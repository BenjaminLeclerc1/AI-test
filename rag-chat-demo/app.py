import streamlit as st
from src.document_loader import DocumentLoader
from src.vector_store import VectorStore
from src.chat_without_rag import SimpleChat
from src.chat_with_rag import RAGChat
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_chats():
    # Chargement des documents depuis S3
    loader = DocumentLoader(os.getenv('AWS_BUCKET_NAME'))
    documents = loader.load_documents()
    
    # Création du vector store
    vector_store = VectorStore()
    vector_store.create_vector_store(documents)
    
    # Initialisation des chats
    simple_chat = SimpleChat(temperature=st.session_state.temperature)
    rag_chat = RAGChat(vector_store, temperature=st.session_state.temperature)
    
    return simple_chat, rag_chat

def main():
    st.title("Démo Chat RAG vs Non-RAG")
    
    if 'temperature' not in st.session_state:
        st.session_state.temperature = 0.7
    
    # Slider pour la température
    st.session_state.temperature = st.slider(
        "Température du modèle",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.temperature,
        step=0.1
    )
    
    # Initialisation des chats
    simple_chat, rag_chat = initialize_chats()
    
    # Interface de chat
    question = st.text_input("Posez votre question:")
    
    if st.button("Obtenir les réponses"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Réponse sans RAG")
            response_simple = simple_chat.get_response(question)
            st.write(response_simple)
            
        with col2:
            st.subheader("Réponse avec RAG")
            response_rag = rag_chat.get_response(question)
            st.write(response_rag)

if __name__ == "__main__":
    main() 