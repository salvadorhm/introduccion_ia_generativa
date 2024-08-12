"""
curl http://localhost:11434/api/chat -d '{
  "model": "gemma:2b",
  "messages": [
    { 
        "role": "user", 
        "content": "¿por qué el cielo es de color azúl?" 
    }
  ],
  "stream":false
}'
"""

import requests

url = 'http://localhost:11434/api/chat' # API de CHAT
data = {
    "model": "gemma:2b",
    "messages": [
        { 
            "role": "user", 
            "content": "¿por qué el cielo es de color azúl?" 
        }
    ],
    "stream":False
    }

r = requests.post(url, json = data)
print(r.text)
