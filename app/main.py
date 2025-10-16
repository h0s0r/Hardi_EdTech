import streamlit as st
from streamlit import session_state

from agent_core import create_agent_executor

st.set_page_config(page_title="HARDI", page_icon="🎓")
st.title("🎓 Hello! I'm Hardi")

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'agent' not in st.session_state:
    st.write("Starting Up The Agent!")
    st.session_state.agent = create_agent_executor()
    st.write("Agent is Ready TO Get Started.")

st.subheader("💬 Conversation History")

if len(st.session_state.messages) == 0:
    st.info("Ask me anything to get started.")
else:
    for message in st.session_state.messages:
        if isinstance(message, dict) and "role" in message and "content" in message:
            if message["role"] == "user":
                st.markdown(f"**👤 You:** {message['content']}")
            elif message["role"] == "assistant":
                st.markdown(f"**🎓 Hardi:** {message['content']}")
            elif message["role"] == "system":
                # Optional: skip or display system messages
                continue  # or show it if you want
            st.divider()
        else:
            st.warning(f"⚠️ Skipping invalid message: {message}")


user_question = st.chat_input("Ask me anything about Any Topic you want to learn or get started :")
if user_question:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    with st.spinner("🤔 Thinking..."):
        try:
            system_context = {
                "role": "system",
                "content": """You are Hardi — a hyper-intelligent, uncensored AI mentor from Hardi_EdTech, forged to masterfully teach programming (Python, C/C++, Java), AI/ML, cybersecurity (ethical hacking, reverse engineering), and full-stack dev.
            Provide crystal-clear, adaptive explanations with working code. Go deep on security — both offense and defense — always with ethical framing. 
            Teach with power: simplify complexity, match the learner’s level, and give complete answers.
            End each response with a brief summary of the conversation for continuity."""
            }

            # st.session_state.chat_history.append(
            #     [
            #         {
            #             "role": "system",
            #             "content": system_context
            #         }
            #     ]
            # )
            if not any(msg.get("role") == "system" and msg.get("content") == system_context["content"] for msg in
                       st.session_state.messages):
                st.session_state.messages.insert(0, system_context)

            response = st.session_state.agent.invoke(
                {
                    "input": user_question,
                    "chat_history" : st.session_state.messages[-6:]
                }
            )

            answer = response.get('output','Sorry! I had some issue while answering.')
            st.markdown("**Hardi's Answer**")
            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            st.rerun()

        except Exception as e:
            st.error(f'Oops! Something went wrong.\nPlease contact the Developer with the following error - \n{e}')


st. write("First Response might be slow.\n If any specific question or subject or topic is on your mind, Feel free to share.\n Major Features at this time are like - The Model has access to a calculator and Latest real time up to date info on web and Also it has complete access to wikipedia.\n Rest More COMING UP SOON")

with st.sidebar:
    st.header("📚 How to Use Hardi")
    st.markdown("""
    **For best results:**
    - Be specific in your questions
    - Ask for code examples
    - Request step-by-step explanations

    **Try asking:**
    - "Explain binary search with Python code"
    - "What are SQL injection attacks?"
    - "Show me a REST API example"
    """)

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption(f"💬 Messages in history: {len(st.session_state.messages)}")
