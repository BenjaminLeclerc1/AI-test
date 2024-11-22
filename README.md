# Mon Chat RAG vs Non-RAG

Voici mon projet de chatbot qui compare les réponses avec et sans RAG. Il peut répondre à des questions en se basant soit sur ses connaissances générales, soit en utilisant vos propres documents PDF.

## Ce qu'il faut avant de commencer

### 1. Python 3.10 ( certaines versions récentes ne fonctionnent pas )
- Va sur [python.org](https://www.python.org/downloads/release/python-3109/)
- **IMPORTANT** : Coche la case "Add Python to PATH" pendant l'installation !

### 2. Un compte AWS
- Crée un compte AWS (https://aws.amazon.com/fr/)
- Va dans S3 et crée un "bucket"
- Crée un dossier "documents" dans ton bucket
- mettre le PDF dedans ( un pdf est obligatoire pour le lancement de l'application )

### 3. Ollama 
- Télécharge  Ollama (https://ollama.ai)
- Lance-le
- Ouvre un terminal et tape :
  
  ```bash
  ollama pull mistral
  ```

## Installation

1. **Clone le projet**
   ```bash
   git clone https://github.com/BenjaminLeclerc1/AI-test.git
   cd rag-chat-demo
   ```

2. **Crée ton environnement virtuel**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
   Si la dernière commande marche pas, essaie avec :
   ```bash
   source .venv/bin/activate
   ```

3. **Installe les packages**
   ```bash
   python -m pip install --upgrade pip
   pip install langchain==0.1.12
   pip install chromadb==0.4.24
   pip install boto3==1.34.69
   pip install python-dotenv==1.0.1
   pip install streamlit==1.32.2
   pip install unstructured==0.12.5
   pip install sentence-transformers==2.5.1
   pip install PyPDF2
   ```

4. **Configure AWS**
   - Crée un fichier `.env` à la racine
   - Mets dedans :
     ```
     AWS_ACCESS_KEY_ID=ta_clé
     AWS_SECRET_ACCESS_KEY=ta_clé_secrète
     AWS_BUCKET_NAME=nom_de_ton_bucket
     ```
   (Tu trouves ces infos dans les "Security credentials" de ton compte AWS)

## Comment ça marche ?

1. **Lance Ollama**

2. **Lance l'app**
   ```bash
   streamlit run app.py
   ```

3. **fonctionaliter : !**
   - le curseur de température
   - Pose des questions
   - Compare les réponses avec/sans RAG
