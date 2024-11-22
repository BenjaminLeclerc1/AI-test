from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import uuid
import logging

class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = None
        
    def create_vector_store(self, documents):        
        if not documents:
            return
            
        try:
            document_ids = [str(uuid.uuid4()) for _ in range(len(documents))]
            
            self.vector_store = Chroma(
                collection_name="my_collection",
                embedding_function=self.embeddings,
                persist_directory="vector_store"
            )
            
            texts = [doc.page_content for doc in documents]
            metadatas = [doc.metadata for doc in documents]
            
            self.vector_store.add_texts(
                texts=texts,
                metadatas=metadatas,
                ids=document_ids
            )
            
            
        except Exception as e:
            raise
        
    def get_relevant_documents(self, query, k=3):
        if not self.vector_store:
            return []
        return self.vector_store.similarity_search(query, k=k) 