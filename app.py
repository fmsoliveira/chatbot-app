import streamlit as st
import requests

API_URL = "http://backend:8000"

st.set_page_config(page_title="Chat Conselheiro", layout="wide")

st.title("📜 Chatbot Conselheiro 🤖")

# Upload de arquivos PDF
st.sidebar.header("📂 Upload de PDFs")
uploaded_file = st.sidebar.file_uploader("Envie um PDF", type=["pdf"])

if uploaded_file:
    files = {"file": (uploaded_file.name,
                      uploaded_file.getvalue(), "application/pdf")}
    response = requests.post(f"{API_URL}/upload/", files=files)
    if response.status_code == 200:
        st.sidebar.success("✅ PDF enviado e processado!")

# Área de chat
st.header("💬 Coloque a sua dúvida")
query = st.text_input("Escreva a sua pergunta:")

if st.button("🔎 Perguntar"):
    if query:
        response = requests.get(f"{API_URL}/ask/", params={"query": query})
        if response.status_code == 200:
            st.write("🧠 **Resposta do chatbot:**")
            st.success(response.json()["response"])
        else:
            st.error("Erro ao procurar a resposta.")
    else:
        st.warning("⚠️ Escreva uma pergunta.")
