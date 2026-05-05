from langchain_core.runnables import RunnablePassthrough


def build_pure_chat_chain(llm, prompt):
    # input question -> prompt -> llm
    return (
        {
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
    )

def build_rag_chat_chain(llm, retriever, prompt):
    # input -> retriever -> prompt -> llm -> output
    return (
        {
            "context": lambda x: "", # fake retriever for testing
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )