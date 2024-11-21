from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class SimpleChat:
    def __init__(self, temperature=0.7):
        self.llm = Ollama(model="mistral", temperature=temperature)
        self.prompt = PromptTemplate(
            input_variables=["question"],
            template="Question: {question}\nRéponse:"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
    def get_response(self, question):
        return self.chain.run(question=question) 