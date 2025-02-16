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

<pre>
<code id="code1">git clone https://github.com/seu-repositorio/chatbot-legalista.git
cd chatbot-legalista</code>
<button onclick="copyToClipboard('code1')">📋 Copiar Código</button>
</pre>

3️⃣ Construir e Iniciar os Containers

<pre>
<code id="code2">docker compose up --build</code>
<button onclick="copyToClipboard('code2')">📋 Copiar Código</button>
</pre>

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
|── entrypoint.sh # script para correr no ollama
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

<pre>
<code id="code3">docker compose down</code>
<button onclick="copyToClipboard('code3')">📋 Copiar Código</button>
</pre>

Para monitorizar logs em tempo real:

<pre>
<code id="code4">docker compose logs -f</code>
<button onclick="copyToClipboard('code4')">📋 Copiar Código</button>
</pre>

📝 Funcionalidades a implementar brevemente

🔐 Autenticação de Utilizadores

🔍 Melhorias na Busca Semântica

💾 Persistência e Histórico de Conversas

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀

📜 Código JavaScript para Copiar Código

Adiciona este script ao fim do README para ativar o botão de cópia no GitHub Pages ou outras plataformas Markdown que suportam HTML + JS:

<script>
  function copyToClipboard(id) {
    var copyText = document.getElementById(id).innerText;
    navigator.clipboard.writeText(copyText);
    alert("Código copiado!");
  }
</script>
