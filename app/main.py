import streamlit as st
import tempfile
import os
from datetime import datetime
from agent_core import create_agent_executor
from educational_prompts import ENHANCED_PERSONAS, get_enhanced_prompt
from knowledge_base import get_knowledge_context

st.set_page_config(
    page_title="Hardi EdTech AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    div[data-testid="stChatMessageContent"] p {
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    defaults = {
        'messages': [],
        'agent': None,
        'selected_persona': "🎓 Teacher",
        'pdf_uploaded': False,
        'pdf_path': None,
        'total_queries': 0,
        'kb_hits': 0
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()

with st.sidebar:
    st.header("⚙️ Configuration")

    selected_persona = st.selectbox(
        "Teaching Mode:",
        options=list(ENHANCED_PERSONAS.keys()),
        index=list(ENHANCED_PERSONAS.keys()).index(st.session_state.selected_persona)
    )

    if selected_persona != st.session_state.selected_persona:
        st.session_state.selected_persona = selected_persona
        st.success(f"✓ {selected_persona}")
        st.rerun()

    st.markdown(f"**Active:** {ENHANCED_PERSONAS[selected_persona]['icon']} {selected_persona}")

    st.divider()

    st.subheader("📄 Document Analysis")
    uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])

    if uploaded_file is not None:
        if not st.session_state.pdf_uploaded or st.session_state.pdf_path is None:
            with st.spinner("Processing..."):
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        st.session_state.pdf_path = tmp_file.name

                    st.session_state.agent = create_agent_executor(pdf_path=st.session_state.pdf_path)
                    st.session_state.pdf_uploaded = True
                    st.success(f"✓ {uploaded_file.name}")
                except Exception as e:
                    st.error(f"✗ Error: {str(e)}")
        else:
            st.info(f"📄 {uploaded_file.name}")

    if st.session_state.pdf_uploaded:
        if st.button("🗑️ Remove PDF", use_container_width=True):
            if st.session_state.pdf_path and os.path.exists(st.session_state.pdf_path):
                try:
                    os.unlink(st.session_state.pdf_path)
                except:
                    pass
            st.session_state.pdf_path = None
            st.session_state.pdf_uploaded = False
            st.session_state.agent = None
            st.rerun()

    st.divider()

    st.subheader("🎯 Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if len(st.session_state.messages) > 0:
            export_text = f"Hardi Chat Export\n{datetime.now()}\n{st.session_state.selected_persona}\n\n"
            for msg in st.session_state.messages:
                role = "YOU" if msg['role'] == 'user' else "HARDI"
                export_text += f"{role}: {msg['content']}\n\n"

            st.download_button(
                "📥 Export",
                data=export_text,
                file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )

    st.divider()

    st.subheader("📊 Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len(st.session_state.messages))
        st.metric("Queries", st.session_state.total_queries)
    with col2:
        st.metric("KB Hits", st.session_state.kb_hits)
        st.metric("PDF", "Yes" if st.session_state.pdf_uploaded else "No")

    st.divider()

    with st.expander("ℹ️ About"):
        st.markdown(f"""
        **Hardi EdTech v1.0**

        Active: {st.session_state.selected_persona}

        Features:
        - 4 Teaching personas
        - Knowledge base
        - Multi-tool support
        - PDF analysis

        Model: GPT-OSS 20B
        """)

persona_color = ENHANCED_PERSONAS[st.session_state.selected_persona]['color']
st.markdown(f"""
<div style='background: linear-gradient(135deg, {persona_color}, {persona_color}cc);
            padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
    <h1 style='color: white; margin: 0; text-align: center;'>
        {ENHANCED_PERSONAS[st.session_state.selected_persona]['icon']} Hardi EdTech
    </h1>
    <p style='color: white; margin: 5px 0 0 0; text-align: center; opacity: 0.9;'>
        {st.session_state.selected_persona}
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

if len(st.session_state.messages) == 0:
    st.info(f"👋 Welcome! I'm in **{st.session_state.selected_persona}** mode. Ask me anything!")
else:
    for message in st.session_state.messages:
        if message.get("role") == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(message['content'])
        elif message.get("role") == "assistant":
            with st.chat_message("assistant", avatar=ENHANCED_PERSONAS[st.session_state.selected_persona]['icon']):
                st.markdown(message['content'])

user_question = st.chat_input("Ask me anything...")

if user_question:
    if st.session_state.agent is None:
        with st.spinner("Initializing..."):
            try:
                st.session_state.agent = create_agent_executor(
                    pdf_path=st.session_state.pdf_path if st.session_state.pdf_uploaded else None
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.stop()

    st.session_state.messages.append({"role": "user", "content": user_question})
    st.session_state.total_queries += 1

    with st.spinner("Thinking..."):
        try:
            enhanced_prompt = get_enhanced_prompt(st.session_state.selected_persona, user_question)
            kb_context = get_knowledge_context(user_question, max_results=2)

            if kb_context:
                enhanced_prompt += kb_context
                st.session_state.kb_hits += 1

            chat_history = [{"role": "system", "content": enhanced_prompt}]
            recent_messages = [msg for msg in st.session_state.messages[-10:] if msg["role"] != "system"]
            chat_history.extend(recent_messages)

            response = st.session_state.agent.invoke({
                "input": user_question,
                "chat_history": chat_history
            })

            answer = response.get('output', 'Error processing request.')
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()

        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.caption(f"🎭 {st.session_state.selected_persona}")
with col2:
    st.caption(f"💬 {len(st.session_state.messages)} messages")
with col3:
    st.caption(f"🧠 Enhanced mode")