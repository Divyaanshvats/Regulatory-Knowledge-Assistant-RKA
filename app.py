import streamlit as st
import os
import sys
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Ensure project root is accessible
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.llm import get_chatgroq_model
from utils.rag_pipeline import build_vector_store, retrieve_context
from utils.web_search import search_web


def get_chat_response(chat_model, messages, system_prompt):
    """Get response from the chat model"""

    try:
        formatted_messages = [SystemMessage(content=system_prompt)]

        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))

        response = chat_model.invoke(formatted_messages)

        return response.content

    except Exception as e:
        return f"Error getting response: {str(e)}"


def instructions_page():
    """Instructions page"""

    st.title("📘 The Chatbot Blueprint")

    st.markdown("""
    ## Setup Instructions

    Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    ### API Keys

    Set your API keys as environment variables.

    **Groq**

    https://console.groq.com/keys

    Example (Windows):

    ```
    setx GROQ_API_KEY "your_key_here"
    ```

    Restart terminal after setting.

    ---

    ## Features Implemented

    ✔ Retrieval Augmented Generation (RAG)  
    ✔ Web search fallback  
    ✔ Concise / Detailed response modes  
    ✔ Source citation support  
    ✔ Streamlit chatbot UI

    Navigate to the **Chat page** to start using the assistant.
    """)

@st.cache_resource
def load_vector_db():
    return build_vector_store()
def chat_page():
    """Main chatbot page"""

    st.title("REGULATORY KNOWLEDGE ASSISTANT (RKA)")

    # Response mode (required by assignment)
    response_mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"],
        horizontal=True
    )

    system_prompt = f"""
    You are an AI compliance assistant specializing in HR policies,
    Indian labour laws, and RBI banking regulations.

    Response style: {response_mode}

    If context is provided, use it to answer accurately.
    Always cite the document source when possible.
    """

    chat_model = get_chatgroq_model()

    # Build vector database once
    if "vector_store" not in st.session_state:
        with st.spinner("Loading documents and building knowledge base..."):
            index, docs = load_vector_db()
            st.session_state.index = index
            st.session_state.docs = docs

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about HR policies, labour law, or RBI regulations..."):

        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Retrieve RAG context
        context_chunks, scores = retrieve_context(
            prompt,
            st.session_state.index,
            st.session_state.docs
        )

# If similarity is poor → use web search
        if scores[0] > 1.0:
            web_results = search_web(prompt)
            context_chunks = web_results

        context_text = "\n\n".join(context_chunks)

        augmented_prompt = f"""
        Use the following context to answer the question.
        If the context is from web search, prioritize it.
        Context:
        {context_text}
        Question:
        {prompt}
        """

        st.session_state.messages.append({"role": "user", "content": augmented_prompt})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response = get_chat_response(
                    chat_model,
                    st.session_state.messages,
                    system_prompt
                )

                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


def main():

    st.set_page_config(
    page_title="Regulatory Knowledge Assistant (RKA)",
        page_icon="🤖",
        layout="wide"
    )

    with st.sidebar:

        st.title("Navigation")

        page = st.radio(
            "Go to:",
            ["Chat", "Instructions"]
        )

        if page == "Chat":
            st.divider()

            if st.button("🗑 Clear Chat History", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

    if page == "Instructions":
        instructions_page()

    if page == "Chat":
        chat_page()


if __name__ == "__main__":
    main()
