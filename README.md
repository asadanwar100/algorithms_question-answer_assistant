# 📁 Algorithms_QA: LangChain RAG with Ollama (Textbook QA)

This repository contains a local Retrieval-Augmented Generation (RAG) setup using LangChain, FAISS, and Ollama running a local model.
The goal is to create a resource for Algorithms classes at the undergraduate and graduate levels. The material used includes information
from Introduction to Algorithms and related texts.

## 🧠 Features
- Uses LangChain's retrieval chain with local FAISS vectorstore
- Embedded using `nomic-embed-text` through Ollama
- Local inference with `gemma3:4b` model via Ollama

---

## ⚙️ Setup Instructions

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/yourusername/langchain-rag-project.git
cd langchain-rag-project
```

### 2. 🐍 Create Conda Environment (Optional but Recommended)
```bash
conda create -n rag_env python=3.10 -y
conda activate rag_env
```

### 3. 🧪 Install Requirements
```bash
pip install -r requirements.txt
```

### 4. 🚀 Set Up Ollama and Pull Models/Embeddings
```bash
bash setup_ollama.sh
```

This script will:
- Install Ollama (if not already installed)
- Pull `gemma3:4b` and `nomic-embed-text` for embedding + inference

### 5. 💾 Vectorstore
The 'vectorstore' directory is included in the repository. It includes information from Introduction to Algorithms and related course material.

---

## 🏃 Run the App

```bash
cd app
python main.py
```

You will:
- Ask a question related to Design and Analysis of Algorithms.
- Receive a detailed, retrieved-context-based answer from the local model.

---

## 📝 Notes
- Book loading and embedding is excluded for privacy and size reasons.
- You **must** use the included `vectorstore` for the application to retrieve from.
- Current

---

## 📁 Files Included

- `app/main.py`: Main script to run QA system
- `requirements.txt`: Python dependencies
- `setup_ollama.sh`: Ollama install and model pull script
- `README.md`: Documentation

---

## 📦 Optional
If you're contributing or modifying:
- Add your own books + `build_vectorstore.py` (excluded from repo)
- Feel free to modify the system prompt in main.py to better handle your requirements.


---

## 📄 License
MIT License
