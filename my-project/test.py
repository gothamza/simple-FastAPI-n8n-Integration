import requests

res = requests.post("http://localhost:8000/ask-llm", json={
    "prompt": "Tell me a fun fact about space."
})

print(res.json())
