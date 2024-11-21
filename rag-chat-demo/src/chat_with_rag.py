from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class RAGChat:
    def __init__(self, vector_store, temperature=0.7):
        self.llm = Ollama(model="mistral", temperature=temperature)
        self.vector_store = vector_store
        
        template = """Utilise le contexte suivant pour répondre à la question.
        
        Contexte: {context}
        
        Question: {question}
        
        Réponse:"""
        
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )
        
        self.chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.vector_store.as_retriever(),
            chain_type_kwargs={"prompt": self.prompt}
        )
        
    def get_response(self, question):
        return self.chain.run(question) 