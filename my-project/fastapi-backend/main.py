from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask-llm")
async def ask_llm(data: PromptRequest):
    payload = {
        "model": MODEL,
        "prompt": data.prompt
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(OLLAMA_URL, json=payload, timeout=60)
            response.raise_for_status()

        lines = response.text.strip().splitlines()
        full_output = "".join([eval(line)["response"] for line in lines if line.strip()])
        return {"response": full_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")
