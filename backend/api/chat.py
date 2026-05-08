from __future__ import annotations

# use Request for dependency injection, gives access to the fast api app
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
import json

# router for chat requests
router = APIRouter(tags=["chat"])


##### Data Contract #####

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1) # Field adds validation: question must be provided (...), a string, and have at least one char
    mode: str = Field(default="default")

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]


##### Endpoints #####

@router.post("/chat", response_model=ChatResponse)
def chat(req:ChatRequest, request: Request) -> ChatResponse:
    chain = request.app.state.chain_registry.get_chain(req.mode)
    result = chain.invoke(req.question)

    answer_text = getattr(result, "content", str(result))
    return ChatResponse(answer=answer_text, sources=[])

@router.post("/chat-stream")
async def chat_stream(req:ChatRequest, request:Request):
    chain = request.app.state.chain_registry.get_chain(req.mode)

    async def generate():
        for chunk in chain.stream(req.question):
            token = getattr(chunk, "content", str(chunk))
            # Server-sent event (SSE) format: "data: <content>\n\n", standard for server-to-client browser streaming
            # Use json encoding to make sure new lines are not dropped
            yield f"data: {json.dumps({'token': token})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")