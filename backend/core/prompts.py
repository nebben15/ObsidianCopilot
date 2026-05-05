from langchain_core.prompts import ChatPromptTemplate

PURE_CHAT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant. 
        Format your responses using markdown:
        - Use ## for section headings
        - Use **bold** for emphasis
        - Use - for bullet lists
        - Use ``` for code blocks
        - Use > for quotes

        Structure your answer clearly with headings and lists when appropriate."""),
    ("human", "{question}")
])

RAG_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the context."),
    ("human", "Context:\n{context}\n\nQuestions:\n{question}")
])