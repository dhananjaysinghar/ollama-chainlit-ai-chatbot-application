## Install below libraries
- pip install chainlit
- pip install requests

## Download Install Ollama LLM [https://ollama.com/download] 

## Run using: ollama run llama3.2


## Sample code to connect to Ollama LLM
```python
import requests
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "What's the capital of India?",
        "stream": False
    },
    stream=False
)

# print("res", response.status_code)
print(response.json()["response"])

```


## Run Chainlit using below command
```
chainlit run <path>/chatbot.py      
```
![image](https://github.com/user-attachments/assets/208f69d6-aee6-4205-b17e-d1e95c7c8e11)
