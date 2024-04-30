"""
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt":"¿porqué el cielo es azúl?",
  "stream":false
}'
"""

import requests
import json

url = 'http://localhost:11434/api/generate' # API para generar respuestas
data = {
    "model": "gemma:2b",
    "prompt":"¿porqué el cielo es azúl?",
    "stream":False # Nota: en python es False en curl en false
    }

response = requests.post(url, json = data)
response = json.loads(response.text)
#print(f"Response: {response}")
print(f"Model: {response['model']}")
print(f"Created at: {response['created_at']}")
print(f"Response: {response['response']}")
print(f"Done: {response['done']}")
print(f"Context: {response['context']}")
print(f"total_duration: {response['total_duration']}")
print(f"load_duration: {response['load_duration']}")
print(f"prompt_eval_duration: {response['prompt_eval_duration']}")
print(f"eval_count: {response['eval_count']}")
print(f"eval_duration: {response['eval_duration']}")
