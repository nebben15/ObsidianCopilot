import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Obsidian Copilot")
st.write("Ask a question.")

question = st.text_input("Your question:", placeholder="Ask me something ...")

if question:
    try:
        response = requests.post(
            f"{API_URL}/chat-stream",
            json={"question": question, "mode": "default"},
            stream=True,
            timeout=30
        )
        response.raise_for_status()

        st.subheader("Answer")
        answer_placeholder = st.empty()
        full_answer = ""

        # stream response and update in real-time
        for line in response.iter_lines(decode_unicode=True): # synchronous streaming, returns bytes by default, use decode for strings
            if line.startswith("data: "):
                # strip data, add to answer, update ui
                token = line[6:]
                full_answer += token
                answer_placeholder.markdown(full_answer)
        
        # raw text expander for debugging
        with st.expander("🔍 Raw response (debug)"):
            st.code(full_answer, language="text")


        # Sources for RAG
        # if data.get("sources"):
        #     st.subheader("Sources")
        #     for source in data["sources"]:
        #         st.write(f"- {source}")
    except requests.exceptions.RequestException as e:
        st.error(f"API error: {e}")
    except Exception as e:
        st.error(f"Error: {e}")