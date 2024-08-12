"""
curl http://localhost:11434/api/chat -d '{
  "model": "gemma:2b",
  "messages": [
    {
      "role": "user",
      "content": "2 + 2"
    },
    {
      "role": "assistant",
      "content": "the answer is 4"
    },
    {
      "role": "user",
      "content": "3 * 3"
    },
    {
      "role": "assistant",
      "content": "the answer is 9"
    },
    {
      "role": "user",
      "content": "10 / 2"
    }
  ],
  "stream":false
}'
"""

import requests
import json

model = "gemma:2b"  # modelo que se utilizara

def chat(new_message):  # Método para enviar el historial del chat y recibir respuesta
    url = 'http://localhost:11434/api/chat'  # URL de la API de ollama
    data = {
        "model": model,  # modelo a utilizar
        "messages": new_message,  # historial de la conversación 
        "stream":False  # Desactiva el stream de cada palabra 
    }

    response = requests.post(url, json = data)  # Envia la solicitud al sernvidor
    response = json.loads(response.text)  # Codifica la respuesta en formato JSON
    print(f"RESPONSE: {response['message']['content']}")  # Imprime solo el contenido de la respuesta
    return response['message']  # Regresa la respuesta del assitente

def main():  # Metodo que controla la ejecución
    messages_history = []  # Variable que almacena el historial de las conversaciones
    while True:  # Repite indefinidamente el chat
        content = input("PROMPT: ")  # Lee el prompt del usuario
        prompt = {  # Formatea el contenido en formato de chat
            "role": "user",
            "content": content
            }
        messages_history.append(prompt) # se aprega la pregunta del usuario
        response = chat(messages_history) # se manda la pregunta y se recibe la respuesta
        messages_history.append(response) # se concatena la respuesa del assitente

if __name__ == "__main__":
    main()  # inicia el programa
