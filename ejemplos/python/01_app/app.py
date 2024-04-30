"""
curl http://localhost:11434/api/chat -d '{
  "model": "gemma:2b",
  "messages": [
    { 
        "role": "user", 
        "content": "¿porqué el cielo es azúl?" 
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
            "content": "¿porqué el cielo es azúl?" 
        }
    ],
    "stream":False
    }

r = requests.post(url, json = data)
print(r.text)
