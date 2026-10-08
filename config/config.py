import os

try:
    import streamlit as st
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
    TAVILY_API_KEY = st.secrets.get("TAVILY_API_KEY")
except:
    GROQ_API_KEY = None
    TAVILY_API_KEY = None

# fallback for local environment variables
GROQ_API_KEY = GROQ_API_KEY or os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = TAVILY_API_KEY or os.getenv("TAVILY_API_KEY")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"