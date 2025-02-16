Chatbot Advisor - WebApp with Docker, FastAPI, and Streamlit

This project implements an advisor chatbot that allows users to upload PDFs containing laws and regulations. The chatbot responds to user questions using a language model (LLM) based on Ollama and stores information in ChromaDB for semantic searches.

📌 Technologies Used

Python 3.11

FastAPI (Backend)

Streamlit (Web Interface)

ChromaDB (Vector Database)

Ollama (Language Model)

Docker & Docker Compose

🚀 How to Use the Project

1️⃣ Install Docker and Docker Compose

🔗 Docker Installation Guide

2️⃣ Clone the Repository

git clone https://github.com/your-repository/chatbot-legalista.git
cd chatbot-legalista

3️⃣ Build and Start the Containers

docker compose up --build

The application will be available at:

Web Interface (Streamlit): http://localhost:8501

API Backend (FastAPI): http://localhost:8000

📂 Project Structure

chatbot-app/
│── backend/
│ │── main.py # FastAPI API
│ │── process.py # PDF Processing
│ │── vector_store.py # Semantic Storage (ChromaDB)
│ │── chat.py # Communication with Ollama
│── app.py # Streamlit Interface
│── Dockerfile.backend # Backend Configuration
|── Dockerfile.streamlit # Frontend Configuration
│── docker-compose.yml # Container Orchestration
│── requirements.txt # Project Dependencies
|── entrypoint.sh # Script for running Ollama
|── readme.md

🛠️ How It Works

🔹 PDF Upload

The user uploads a PDF file via Streamlit.

The backend (FastAPI) processes and extracts text from the PDF.

The text is converted into embeddings and stored in ChromaDB.

🔹 Chatbot Query

The user asks a question in Streamlit.

The backend searches ChromaDB for relevant parts of the PDFs.

The retrieved elements are sent to Ollama, which generates a response.

The response is sent to the user via Streamlit.

📡 Communication Between Services

FastAPI communicates with:

ChromaDB (http://chromadb:8000) for context searches.

Ollama (http://ollama:11434) to generate responses.

Streamlit interacts with FastAPI to send questions and receive responses.

🛑 Stopping the Containers

docker compose down

To monitor logs in real time:

docker compose logs -f

📝 Upcoming Features

🔐 User Authentication

🔍 Improved Semantic Search

💾 Persistence and Conversation History

If you have any questions or suggestions, feel free to contribute! 🚀 If you can't help, just make some noise, the important thing is to participate! 😜

📖 Versão em Português

Chatbot Conselheiro - WebApp com Docker, FastAPI e Streamlit

Este projeto implementa um chatbot conselheiro que permite o upload de PDFs com leis e regulamentos. O chatbot responde a perguntas do utilizador através de um modelo de linguagem (LLM) baseado no Ollama e guarda informações em ChromaDB para buscas semânticas.

📌 Tecnologias Utilizadas

Python 3.11

FastAPI (Backend)

Streamlit (Interface Web)

ChromaDB (Banco de dados vetorial)

Ollama (Modelo de linguagem)

Docker & Docker Compose

🚀 Como utilizar o Projeto

1️⃣ Instalar o Docker e Docker Compose

🔗 Guia de Instalação do Docker

2️⃣ Clonar o Repositório

git clone https://github.com/seu-repositorio/chatbot-legalista.git
cd chatbot-legalista

3️⃣ Construir e Iniciar os Containers

docker compose up --build

A aplicação estará disponível em:

Interface Web (Streamlit): http://localhost:8501

API Backend (FastAPI): http://localhost:8000

📂 Estrutura do Projeto

chatbot-app/
│── backend/
│ │── main.py # API FastAPI
│ │── process.py # Processamento de PDFs
│ │── vector_store.py # Armazenamento semântico (ChromaDB)
│ │── chat.py # Comunicação com Ollama
│── app.py # Interface Streamlit
│── Dockerfile.backend # Configuração do backend
|── Dockerfile.streamlit # Configuração do frontend
│── docker-compose.yml # Orquestração dos containers
│── requirements.txt # Dependências do projeto
|── entrypoint.sh # Script para correr no Ollama
|── readme.md

🛠️ Como Funciona

🔹 Upload de PDFs

O utilizador envia um arquivo PDF via Streamlit.

O backend (FastAPI) processa e extrai o texto do PDF.

O texto é convertido em embeddings e armazenado no ChromaDB.

🔹 Consulta ao Chatbot

O utilizador faz uma pergunta no Streamlit.

O backend procura no ChromaDB partes relevantes dos PDFs.

Os elementos são enviados para o Ollama, que gera uma resposta.

A resposta é enviada ao utilizador via Streamlit.

📡 Comunicação entre Serviços

FastAPI comunica com:

ChromaDB (http://chromadb:8000) para pesquisas de contexto.

Ollama (http://ollama:11434) para gerar respostas.

Streamlit interage com o FastAPI para enviar perguntas e receber respostas.

🛑 Parar os Containers

docker compose down

Para monitorizar logs em tempo real:

docker compose logs -f

📝 Funcionalidades a implementar brevemente

🔐 Autenticação de Utilizadores

🔍 Melhorias na Busca Semântica

💾 Persistência e Histórico de Conversas

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀 Se não puder ajudar, atrapalhe, o importante é participar! 😜
