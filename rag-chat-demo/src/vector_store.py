from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = None
        
    def create_vector_store(self, documents):
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory="vector_store"
        )
        self.vector_store.persist()
        
    def get_relevant_documents(self, query, k=3):
        return self.vector_store.similarity_search(query, k=k) 