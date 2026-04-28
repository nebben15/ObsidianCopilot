import streamlit as st
import requests
import re

DEBUG = True

####### Helpers ######

def last_message(role):
    for msg in reversed(st.session_state.messages):
        if msg["role"] == role:
            return msg
    return None


def render_md(text: str) -> str:
    # Fix headings (##, ###, etc.)
    text = re.sub(r"(##+)", r"\n\n\1", text)

    # Ensure newline AFTER headings
    text = re.sub(r"(##+[^\n]+)", r"\1\n\n", text)

    # Fix horizontal rules
    text = re.sub(r"---+", r"\n\n---\n\n", text)

    # Fix bullet points
    text = re.sub(r"([^\n])\n?(-|\*) ", r"\1\n\n\2 ", text)

    # Fix code blocks
    text = re.sub(r"```(\w+)?([^\n])", r"```\1\n\2", text)

    # Normalize spacing
    text = text.replace("\n", "\n\n")

    return text

####### Script #######

st.title("Obsidian Copilot")

# create message history -- initiallize with system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """You are an AI assistant helping the user with any question.
                        Rules:
                        - Always format responses in clean Markdown
                        - Use blank lines between sections
                        - Put headings on their own line, so add a newline after every heading
                        - Use bullet lists with proper spacing
                        - Never write things like "---##" on the same line
                        - Use headings, lists, and code blocks when appropriate
                        - Be concise but clear"""
        }
    ]

# render
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    # render as markdown
    with st.chat_message(msg["role"]):
        st.markdown(render_md(msg["content"]))

if DEBUG and (last_assistant := last_message("assistant")):
    with st.expander("🔍 Last assistant message (raw)"):
        st.code(last_assistant["content"])


# update state
if prompt := st.chat_input("Input"):
    # add prompt to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display user message
    st.chat_message("user").write(prompt)

    # receive response stream
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        with requests.post(
            "http://localhost:8000/chat-stream",
            json={"messages": st.session_state.messages},
            stream=True
        ) as res:

            # render stream as it comes in
            for chunk in res.iter_lines():
                if chunk:
                    token = chunk.decode()
                    full_response += token
                    placeholder.markdown(full_response)

        # add response to history
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
        
    # rerun to render cleanely once response is fully streamed
    st.rerun()