# Chatbot Conselheiro - WebApp com Docker, FastAPI e Streamlit

Este projeto implementa um chatbot conselheiro que permite o upload de PDFs com leis e regulamentos. O chatbot responde a perguntas do utilizador através de um modelo de linguagem (LLM) baseado no **Ollama** e guarda informações em **ChromaDB** para buscas semânticas.

## 📌 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI** (Backend)
- **Streamlit** (Interface Web)
- **ChromaDB** (Banco de dados vetorial)
- **Ollama** (Modelo de linguagem)
- **Docker & Docker Compose**

---

## 🚀 Como utilizar o Projeto

### 1️⃣ Instalar o Docker e Docker Compose

🔗 [Guia de Instalação do Docker](https://docs.docker.com/get-docker/)

### 2️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-repositorio/chatbot-legalista.git
cd chatbot-legalista
```

### 3️⃣ Construir e Iniciar os Containers

```bash
docker compose up --build
```

A aplicação estará disponível em:

- **Interface Web (Streamlit):** [http://localhost:8501](http://localhost:8501)
- **API Backend (FastAPI):** [http://localhost:8000](http://localhost:8000)

---

## 📂 Estrutura do Projeto

```
chatbot-app/
│── backend/
│   │── main.py          # API FastAPI
│   │── process.py       # Processamento de PDFs
│   │── vector_store.py  # Armazenamento semântico (ChromaDB)
│   │── chat.py          # Comunicação com Ollama
│── app.py               # Interface Streamlit
│── Dockerfile.backend   # Configuração do backend
|── Dockerfile.streamlit # Configuração do frontend
│── docker-compose.yml   # Orquestração dos containers
│── requirements.txt     # Dependências do projeto
|── entrypoint.sh        # script para correr no ollama
|── readme.md
```

---

## 🛠️ Como Funciona

### 🔹 Upload de PDFs

1. O utilizador envia um arquivo PDF via **Streamlit**.
2. O **backend (FastAPI)** processa e extrai o texto do PDF.
3. O texto é convertido em embeddings e armazenado no **ChromaDB**.

### 🔹 Consulta ao Chatbot

1. O utilizador faz uma pergunta no **Streamlit**.
2. O **backend** procura no **ChromaDB** partes relevantes dos PDFs.
3. Os elementos são enviados para o **Ollama**, que gera uma resposta.
4. A resposta é enviada ao utilizador via **Streamlit**.

---

## 📡 Comunicação entre Serviços

1. **FastAPI** comunica com:

   - **ChromaDB** (`http://chromadb:8000`) para pesquisas de contexto.
   - **Ollama** (`http://ollama:11434`) para gerar respostas.

2. **Streamlit** interage com o **FastAPI** para enviar perguntas e receber respostas.

---

## 🛑 Parar os Containers

```bash
docker compose down
```

Para monitorizar logs em tempo real:

```bash
docker compose logs -f
```

---

## 📝 Funcionalidades a implementar brevemente

- 🔐 **Autenticação de Utilizadores**
- 🔍 **Melhorias na Busca Semântica**
- 💾 **Persistência e Histórico de Conversas**

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀 Se não puder ajudar, atrapalhe, o importante é participar! 😜
