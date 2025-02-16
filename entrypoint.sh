#!/bin/sh

# Inicia o Ollama como servidor em background
ollama serve &

# Aguarda um momento para garantir que o servidor arranca corretamente
sleep 5

# Faz o download do modelo se ainda não estiver disponível
ollama pull llama3

# Carrega o modelo para estar pronto a responder
ollama run llama3

# Mantém o container ativo
tail -f /dev/null
