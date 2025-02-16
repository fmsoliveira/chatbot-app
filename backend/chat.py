import requests

OLLAMA_URL = "http://ollama:11434/api/generate"

def chat_with_ollama(context, query):
    payload = {
        "model": "llama3",  # Define explicitamente o modelo
        "prompt": f"Contexto:\n{context}\n\nPergunta: {query}",
        "stream": False  # Define se queres streaming ou resposta completa
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(OLLAMA_URL, json=payload, headers=headers)

    try:
        response_json = response.json()
        return response_json.get("response", "Erro: resposta inválida do Ollama.")
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to decode JSON response:", e)
        print("Response content:", response.content)
        return "Erro: Falha ao processar resposta do Ollama."
