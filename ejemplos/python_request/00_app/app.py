"""
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt":"¿por qué el cielo es de color azúl?",
  "stream":false
}'
"""

import requests

url = 'http://localhost:11434/api/generate' # API para generar respuestas
data = {
    "model": "gemma:2b",
    "prompt":"¿porqué el cielo es azúl?",
    "stream":False
    }

r = requests.post(url, json = data)
print(r.text)
