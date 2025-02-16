from fastapi import FastAPI, UploadFile
import uuid
import os
from backend import process
from backend import vector_store
from backend import chat

UPLOAD_FOLDER = "uploads"

app = FastAPI(
    title="Backend bot conselheiro",
    description="API para processamento de perguntas com Ollama",
    version="1.0.0"
)


@app.post("/upload/")
async def upload_pdf(file: UploadFile):
    content = await file.read()

    # Criar a pasta se não existir
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER,f"{uuid.uuid4()}.pdf")

    with open(file_path, "wb") as f:
        f.write(content)

    text = process.extract_text_from_pdf(file_path)
    vector_store.add_document(text, file_path)
    return {"message": "PDF processado com sucesso"}


@app.get("/ask/")
def ask(query: str):
    relevant_docs = vector_store.search_similar(query)
    context = "\n".join(relevant_docs)
    response = chat.chat_with_ollama(context, query)
    return {"response": response}