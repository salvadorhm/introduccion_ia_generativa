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

url = 'http://localhost:11434/api/chat' # API de CHAT
data = {
    "model": "gemma:2b",
    "messages": [
        {
            "role": "user",
            "content": "2 + 2"
        },
        {
            "role": "assistant",
            "content": "the answer is: 4"
        },
        {
            "role": "user",
            "content": "3 * 3"
        },
        {
            "role": "assistant",
            "content": "the answer is: 9"
        },
        {
            "role": "user",
            "content": "10 / 2"
        }
    ],
    "stream":False
    }

response = requests.post(url, json = data)
response = json.loads(response.text)
#print(f"Response: {response}")
print(f"Response: {response['message']['content']}")
