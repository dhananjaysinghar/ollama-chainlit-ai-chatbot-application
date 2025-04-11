## Install below libraries
- pip install chainlit
- pip install requests

## Download Install Ollama [https://ollama.com/download] 

## Run using: ollama run llama3.2

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "What's the capital of France?",
        "stream": False
    },
    stream=False
)

# print("res", response.status_code)
print(response.json()["response"])

```
