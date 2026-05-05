from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.chat import router as chat_router
from backend.chains.chain_registry import ChainRegistry

# startup/shutdown hook -> build chain registry
@asynccontextmanager
async def lifespan(app: FastAPI): # async to allow await during startup
	# start up
	registry = ChainRegistry()
	registry.initialize()
	app.state.chain_registry = registry # add registry to app state (FastAPI app storage area)
	yield
	# shut down

app = FastAPI(title="Obsidian Copilot API", version="0.1.0", lifespan=lifespan)
app.include_router(chat_router)


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}