from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class RAGChat:
    def __init__(self, vector_store, temperature=0.7):
        print("Initializing RAGChat...")  # Debug log
        self.llm = Ollama(model="mistral", temperature=temperature)
        self.vector_store = vector_store
        
        if not self.vector_store.vector_store:
            raise ValueError("Vector store not properly initialized!")
            
        template = """Utilise le contexte suivant pour répondre à la question.
        
        Contexte: {context}
        
        Question: {question}
        
        Réponse:"""
        
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )
        
        try:
            self.chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.vector_store.as_retriever(),
                chain_type_kwargs={"prompt": self.prompt}
            )
        except Exception as e:
            raise
        
    def get_response(self, question):
        if not self.chain:
            return "Error: Chat system not properly initialized"
        try:
            return self.chain.run(question)
        except Exception as e:
            return f"Error generating response: {str(e)}" 