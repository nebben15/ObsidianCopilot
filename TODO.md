## Core Tech Stack

- FastAPI backend
- LangChain + Qdrant for RAG
- Streamlit frontend for testing
- Ollama for local LLMs (later OpenAI API)
- Integration as Obisidian extension

## Structure

obsidian-copilot/\
│\
├── backend/                          (Backend application logic)\
│   │\
│   ├── api/                          (FastAPI route handlers / endpoints)\
│   │   └── chat.py                   (/chat endpoint – entrypoint for requests)\
│   │\
│   ├── chains/                       (LangChain orchestration layer)\
│   │   └── chat_chain.py             (Main RAG pipeline: retriever → prompt → LLM)\
│   │\
│   ├── core/                         (Core configuration and prompts)\
│   │   ├── config.py                 (Global settings: model names, paths, etc.)\
│   │   └── prompts.py                (System + RAG prompt templates)\
│   │\
│   ├── db/                           (Database / vector store connections)\
│   │   └── qdrant_client.py          (Qdrant client setup and access)\
│   │\
│   ├── models/                       (Data schemas / validation)\
│   │   └── schemas.py                (Pydantic request/response models)\
│   │\
│   ├── services/                     (Low-level reusable components)\
│   │   ├── embeddings.py             (Embedding model + utilities)\
│   │   ├── llm.py                    (Ollama / LLM wrapper)\
│   │   ├── memory.py                 (Chat memory handling)\
│   │   └── rag.py                    (Retriever + RAG helper logic)\
│   │\
│   └── main.py                       (FastAPI app entrypoint)\
│\
├── ingestion/                        (Offline data processing pipeline)\
│   ├── loader.py                     (Load Obsidian markdown files)\
│   ├── chunking.py                   (Split documents into chunks)\
│   ├── embed.py                      (Generate embeddings)\
│   └── index.py                      (Store embeddings in Qdrant)\
│\
├── ui/                               (Frontend code)\
│   └── app.py                        (Streamlit chat interface)\
│\
├── docker/                           (Containerization / deployment setup)\
│   └── Dockerfile                    (Docker build config)\
│\
├── data/                             (Local data storage – optional but recommended)\
│   └── obsidian_notes/               (Your vault / markdown files)\
│\
├── requirements.txt                  (Python dependencies)\
├── README.md                         (Project documentation)\
├── TODO.md                           (Development roadmap)\
└── LICENSE                           (License file)\
