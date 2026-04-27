## Core Tech Stack (Stage 1)

- FastAPI backend
- LangChain + Pinecone for RAG
- Streamlit frontend

## Structure

obsidian-ai-agent/
│
├── backend/                     # FastAPI backend
│   ├── main.py                 # app entrypoint
│
│   ├── api/                    # API routes
│   │   └── chat.py
│
│   ├── core/                   # config + settings
│   │   └── config.py
│
│   ├── services/               # 💡 core logic (most important)
│   │   ├── llm/
│   │   │   ├── base.py         # interface
│   │   │   ├── local.py        # local model (Ollama etc.)
│   │   │   └── remote.py       # OpenAI etc. (future)
│   │   │
│   │   ├── rag/
│   │   │   ├── embedder.py
│   │   │   ├── retriever.py
│   │   │   └── pipeline.py
│   │   │
│   │   ├── vectordb/
│   │   │   └── qdrant_client.py
│   │   │
│   │   └── agent/              # future (LangGraph)
│   │       └── agent.py
│
│   ├── models/                 # request/response schemas
│   │   └── schemas.py
│
│   └── utils/
│       └── loaders.py
│
├── ui/                         # Streamlit frontend
│   └── app.py
│
├── data/                       # local docs / Obsidian vault
│
├── scripts/                    # ingestion + indexing
│   └── ingest.py
│
├── docker/                     # infra configs
│   ├── docker-compose.yml      # Qdrant + backend later
│   └── Dockerfile
│
├── .env
├── requirements.txt
└── README.md