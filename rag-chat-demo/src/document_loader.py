import boto3
from langchain.document_loaders import S3DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging
import os
from langchain.schema import Document
from PyPDF2 import PdfReader
import io

class DocumentLoader:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')
        
    def extract_text_from_pdf(self, pdf_content):
        """Extrait le texte d'un PDF sans utiliser Poppler"""
        pdf_file = io.BytesIO(pdf_content)
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
        
    def load_documents(self):
        try:
            print(f"\nChargement des documents depuis S3...")
            
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix='documents/'
            )
            
            if 'Contents' not in response:
                print("Aucun document trouvé dans le bucket!")
                return []
            
            all_docs = []
            for obj in response['Contents']:
                if obj['Key'].endswith('.pdf'):
                    print(f"Traitement de: {obj['Key']}")
                    
                    response = self.s3_client.get_object(
                        Bucket=self.bucket_name,
                        Key=obj['Key']
                    )
                    pdf_content = response['Body'].read()
                    
                    # Extraire le texte
                    text = self.extract_text_from_pdf(pdf_content)
                    
                    doc = Document(
                        page_content=text,
                        metadata={"source": obj['Key']}
                    )
                    all_docs.append(doc)
            
            print(f"\nNombre de documents chargés: {len(all_docs)}")
            
            if not all_docs:
                print("Attention: Aucun document PDF n'a été trouvé!")
                return []
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            
            split_docs = text_splitter.split_documents(all_docs)
            print(f"Documents divisés en {len(split_docs)} chunks")
            
            return split_docs
            
        except Exception as e:
            print(f"\nErreur lors du chargement des documents: {str(e)}")
            raise