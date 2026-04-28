## Core Tech Stack

- FastAPI backend
- LangChain + Pinecone for RAG
- Streamlit frontend for testing
- Integration as Obisidian extension

## Structure

obsidian-copilot/
│
├── frontend/
│   └── app.py                  # Streamlit UI
│
├── backend/
│   ├── main.py                # FastAPI entrypoint
│
│   ├── api/
│   │   └── chat.py            # /chat endpoint
│
│   ├── core/
│   │   ├── config.py          # settings (model, paths, etc.)
│   │   ├── prompts.py         # system + RAG prompts
│   │
│   ├── services/
│   │   ├── llm.py             # Ollama wrapper
│   │   ├── memory.py          # chat memory
│   │   ├── rag.py             # retrieval pipeline
│   │   └── embeddings.py      # embedding model
│   │
│   ├── chains/
│   │   └── chat_chain.py      # LangChain pipeline
│   │
│   ├── models/
│   │   └── schemas.py         # Pydantic models (input/output)
│   │
│   └── db/
│       └── qdrant_client.py   # vector DB connection
│
├── ingestion/
│   ├── loader.py              # load Obsidian notes
│   ├── chunking.py            # split into chunks
│   ├── embed.py               # generate embeddings
│   └── index.py               # push to Qdrant
│
├── data/
│   └─

## Roadmap

### PHASE 1 — MVP
Goal: “Chat with my Obsidian notes”
Core TODOs
1. Chat system
    - ✅ Streamlit chat UI
    - ✅ FastAPI backend
    - ✅ Ollama integration
    - ✅ Streaming responses
2. Clean message handling
    - ✅ Move system prompt into initialization
    - ✅ Filter system messages from UI
    - ✅ Add debug mode (raw vs rendered output)
    - Basic markdown sanitizer
3. Add memory (short-term)
    - Store chat history in backend (not just frontend)
    - Limit context window (e.g. last N messages)
    - Optional: summarize old messages
4. Build RAG for Obsidian
    - Load Obsidian vault (Markdown files)
    - Chunk documents
    - Generate embeddings
    - Store in vector DB (Qdrant)
5. Retrieval pipeline
    - Query → embedding
    - Similarity search
    - Inject context into prompt (User → retrieve notes → augment prompt → LLM)
6. Prompt engineering for RAG
    - Add system prompt:
        “Use the provided context”
        “If unsure, say you don’t know”
    - Show retrieved documents in debug panel

### PHASE 2 — System Quality & Structure
Goal: “Make the system reliable and closer to production patterns”

1. Structured output experiments
    - Explore different output formats:
    - Markdown (current)
    - JSON
    - YAML
    - Implement basic JSON output mode
    - Compare:
        raw Markdown vs structured JSON → rendered Markdown
        Add toggle in UI for output mode
2. Output parsing & validation
    - Add simple parser for structured output
    - Define schema (e.g. with Pydantic)
    - Validate model responses
    - Handle invalid outputs:
    - retry with adjusted prompt
    - fallback to raw text
    - Optional: implement “output fixing” step
3. Prompt management
    - Move prompts to backend (centralized)
    - Create reusable prompt templates:
        - chat
        - RAG
        - structured output
    - Add prompt versioning (simple config file)
4. Memory upgrade (backend-owned)
    - Move chat history fully to backend
    - Introduce session IDs
    - Implement:
        - sliding window memory (last N messages)
        - optional summarization of older messages
    - Add debug view:
        - current context sent to model
5. RAG improvements
    - Improve chunking: fixed-size vs semantic chunks
    - Add metadata:
        - file name
        - note tags
        - links between notes
    - Improve retrieval:
        - top-k tuning
        - similarity threshold
        - Display retrieved chunks in UI
6. Observability & debugging
    - Log:
        - prompts
        - responses
        - retrieved documents
    - Add latency tracking
    - Add debug panel:
        - raw model output
        - formatted output
        - retrieved context

### PHASE 3 — Agents & Workflows
Goal: “Turn the system into an intelligent assistant”
1. Introduce LangChain / LangGraph
    - Replace manual message handling with:
        - ChatPromptTemplate
        - message abstractions
        - Integrate memory modules
    - Compare:
        manual pipeline vs LangChain pipeline
2. Tool integration (first step to agents)
    - Define tools:
        - search Obsidian notes
        - open specific note
        - create new note
    - Implement tool calling manually (before framework)
3. Agent loop
    - Implement basic loop:
        - user input
        - decide action
        - call tool
        - update state
        - respond
    - Then replicate with LangGraph
4. Multi-step reasoning
    - Add planning step:
        “what should I do?”
    - Execute steps sequentially
    - Compare:
        “thinking models” vs explicit control flow
5. RAG + agent integration
    - Allow agent to:
        - decide when to retrieve
        - choose which notes to use
    - Add “search strategy” logic
6. Experimentation layer
    - Compare:
        - single-shot vs multi-step
        - RAG vs no-RAG
        - structured vs unstructured output
    - Log results for analysis

### PHASE 4 — Productization & Integration
Goal: “Make it portfolio-ready and realistic”

1. UI improvements
    - Improve chat UX:
        - proper Markdown rendering
        - code blocks
        - copy buttons
    - Show sources for RAG answers
    - Add toggles:
        - debug mode
        - model selection
        - output format
2. Model abstraction layer
    - Support:
        - local models (Ollama)
        - hosted APIs (e.g. OpenAI-style)
    - Create unified interface:
        - same input/output format
    - Add model switcher in UI
3. Persistence & storage
    - Store:
        - chat sessions
        - embeddings
        - metadata
    - Optional:
        - simple database (SQLite/Postgres)
4. Obsidian plugin integration
    - Build minimal plugin:
        - send note → backend
        - insert generated content
    - Add features:
        - “summarize note”
        - “generate links”
        - “improve note”
5. - Deployment
    - Dockerize backend
    - Add environment config
    - Optional:
        - deploy to cloud (Render / Fly.io)
        - (Later) explore Kubernetes basics
6. Documentation & portfolio
    - Write strong README:
        - architecture diagram
        - features
        - tech stack
        - Add demo GIF / screenshots
    - Explain:
        - design decisions
        - tradeoffs