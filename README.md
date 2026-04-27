# Obsidian Copilot
AI copilot for the Obisidian note taking app .


## First time setup
Before running the copilot, create a python venv at the root of the repository:
```bash
python3.12 -m venv venv
```
Activate the venv with:
```bash
source venv/bin/activate
```
Then install the requirements:
```bash
pip install -r requirements.txt
```
The copilot uses Ollama for model management and inference. Install it with:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull the model you wish to use:
```bash
ollama pull llama3.1:8b
```

## Running The Application

Always make sure to be in the root folder of the repository, and have the venv active:
```bash
source venv/bin/activate
```

Start the frontend:
```bash
streamlit run ui/app.py
```
Run the API server for the backend:
```bash
uvicorn backend.main:app
```
During development add auto reload:
```bash
uvicorn backend.main:app --reload
```
Run Ollama:
```bash
ollama serve
```