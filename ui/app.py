import streamlit as st
import requests

st.title("Obsidian Copilot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# render
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# update state
if prompt := st.chat_input("Input"):
    # add prompt to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display user message
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        with requests.post(
            "http://localhost:8000/chat-stream",
            json={"messages": st.session_state.messages},
            stream=True
        ) as res:

            for chunk in res.iter_lines():
                if chunk:
                    token = chunk.decode()
                    full_response += token
                    placeholder.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
        
    st.rerun()