from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RewriteRequest(BaseModel):
    prompt: str
    email: str
    provider: str = "openai"  # "openai", "deepseek", "perplexity"

@app.post("/rewrite")
async def rewrite_email(req: RewriteRequest):
    prompt_text = f"{req.prompt.strip()}\n\nEmail:\n{req.email.strip()}"

    try:
        if req.provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "You are a helpful email assistant."},
                    {"role": "user", "content": prompt_text}
                ]
            }
            response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)

        elif req.provider == "deepseek":
            api_key = os.getenv("DEEPSEEK_API_KEY")
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt_text}]
            }
            response = requests.post("https://api.deepseek.com/v1/chat/completions", json=payload, headers=headers)

        elif req.provider == "perplexity":
            api_key = os.getenv("PERPLEXITY_API_KEY")
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            payload = {
                "model": "mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt_text}]
            }
            response = requests.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers)

        else:
            return {"error": "Unsupported provider."}

        response.raise_for_status()
        rewritten = response.json()["choices"][0]["message"]["content"]
        return {"rewritten_email": rewritten.strip()}

    except Exception as e:
        return {"error": str(e)}
