from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
import requests
import ollama

app =FastAPI()

# OLLAMA_URL = "http://localhost:11434/api/generate"

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "llama3.1:8b"

@app.post("/chat")
def chat(req: ChatRequest):
    # naive way
    # response = requests.post(
    #     OLLAMA_URL,
    #     json={
    #         "model": req.model,
    #         "prompt": req.prompt,
    #         "stream": False
    #     }
    # )

    # data = response.json()

    # return {
    #     "response": data["response"]
    # }


    # pythonic way (ollama sdk)
    response = ollama.generate(
        model=req.model,
        prompt=req.prompt
    )
    return response

@app.post("/chat-stream")
def chat_stream(req: ChatRequest):
    # stream generator
    def generate():
        stream = ollama.chat(
            model = req.model,
            messages=req.messages,
            stream=True
        )

        for chunk in stream:
            yield chunk["message"]["content"]
    
    return StreamingResponse(generate(), media_type="text/plain")