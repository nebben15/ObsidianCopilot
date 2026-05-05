from __future__ import annotations

from backend.chains.chat_chain import build_pure_chat_chain, build_rag_chat_chain
from backend.core.prompts import PURE_CHAT_PROMPT, RAG_PROMPT
from backend.services.llm import get_llm

# central chain management
class ChainRegistry:
    def __init__(self) -> None:
        self._cache: dict[str, object] = {}
    
    def initialize(self) -> None:
        # simply use pure chain for now
        llm = get_llm()
        self._cache["default"] = build_pure_chat_chain(llm=llm, prompt=PURE_CHAT_PROMPT)
    
    def get_chain(self, mode: str = "default"):
        if mode not in self._cache:
            raise ValueError(f"Unknown chain mode: {mode}")
        return self._cache[mode]