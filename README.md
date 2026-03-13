# Regulatory Knowledge Assistant (RKA)

A **domain-specific Retrieval-Augmented Generation (RAG) system** designed to answer regulatory and policy-related queries using official documents such as **Indian labour laws, RBI banking guidelines, and HR policy documents**, with **web search fallback for real-time information**.

Live App:
https://regulatory-knowledge-assistant-rka-q2q7paevuqr2lqvakz7hx9.streamlit.app/

---

# Project Name

**Regulatory Knowledge Assistant (RKA)**

---

# Why I Chose This Project

NeoStats works with organizations that often need **accurate answers from regulatory documents such as labour laws, banking guidelines, and HR policies**. These documents are typically lengthy and complex, making it difficult for users to quickly retrieve relevant information.

To address this challenge, I designed a **domain-specific Retrieval-Augmented Generation (RAG) application** that can retrieve relevant knowledge from regulatory documents and provide precise answers.

The core idea behind the project was:

* Reuse publicly available regulatory data and make it useful for clients.
* Focus on documents relevant to **NeoStats’ potential client ecosystem**, such as banking regulations and HR policies.
* Build a system that can answer questions such as:

Example query:

```
What is the gratuity rule after 5 years?
```


To achieve this, the system:

1. Uses publicly available documents such as:

   * Indian Labour Law Handbook
   * RBI Guidelines
   * Payment of Gratuity Act
   * HR Policy documents

2. Converts these documents into embeddings and stores them in a vector database.

3. Retrieves relevant context when a user asks a question.

4. Sends the retrieved context to a Large Language Model (LLM) for generating accurate responses.

5. Falls back to **web search** if the knowledge is not present in the document corpus.

6. Provides a **simple web interface using Streamlit** for user interaction.

This approach demonstrates how NeoStats could build **intelligent knowledge assistants for regulatory or compliance-heavy industries**, enabling faster access to important information.

The complete solution — from development to deployment — was designed to be implemented within a short development cycle.

---

# Basic Architecture of the Model

The system follows a **Retrieval-Augmented Generation (RAG)** architecture.

```
User Question
      │
      ▼
Embedding Query
      │
      ▼
Vector Database Search
      │
      ├── Relevant documents found → Send to LLM
      │
      └── No relevant documents
              │
              ▼
         Web Search (Tavily)
              │
              ▼
         Send results to LLM
              │
              ▼
           Final Answer
```

This architecture ensures that:

* The system answers using **trusted regulatory documents whenever possible**
* If knowledge is missing, **real-time web search provides updated information**

---

# Overall Configuration (Project Structure)

The system is organized into modular components for scalability and maintainability.

```
NeoStats AI Engineer Use Case
│
└── AI_UseCase
    │
    ├── config
    │     └── config.py
    │
    ├── data
    │     ├── gratuity_act.pdf
    │     ├── hr_policy.pdf
    │     ├── labour_law.pdf
    │     └── rbi_guidelines.pdf
    │
    ├── models
    │     ├── embeddings.py
    │     └── llm.py
    │
    ├── utils
    │     ├── document_loader.py
    │     ├── rag_pipeline.py
    │     └── web_search.py
    │
    ├── app.py
    ├── requirements.txt
    └── NeoStats AI Engineer Case Study.pdf
```

### Module Explanation

**config/**

* Stores environment configuration and API keys.

**data/**

* Contains regulatory documents used for knowledge retrieval.

**models/**

* Contains embedding models and LLM configuration.

**utils/**

* Handles document loading, RAG pipeline logic, and web search functionality.

**app.py**

* Streamlit application that provides the user interface.

---

# Environment Requirements

The system requires the following Python packages:

```
streamlit
langchain-openai
langchain-groq
langchain-google-genai
langchain-core
langchain-community
sentence-transformers
faiss-cpu
pypdf
tavily-python
python-dotenv
groq
```

These can be installed using:

```
pip install -r requirements.txt
```

---

# How to Run the Project Locally

### 1. Clone the repository

```
git clone https://github.com/Divyaanshvats/Regulatory-Knowledge-Assistant-RKA.git
```

Navigate into the project:

```
cd Regulatory-Knowledge-Assistant-RKA
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Set API Keys

Set environment variables for the required APIs.

Example (Windows):

```
setx GROQ_API_KEY "your_key_here"
setx TAVILY_API_KEY "your_key_here"
```

Restart the terminal after setting environment variables.

---

### 4. Run the Streamlit Application

```
streamlit run app.py
```

Open the browser at:

```
http://localhost:8501
```

---

# Features Implemented

* Retrieval-Augmented Generation (RAG)
* Vector database using FAISS
* SentenceTransformer embeddings
* LLM integration using Groq
* Web search fallback using Tavily
* Streamlit-based web interface
* Domain-specific regulatory knowledge base

---

# Example Queries

```
What is the gratuity rule after 5 years?
```

```
What deductions are allowed from wages?
```

```
Can banks give loans to their directors?
```

```
What is the latest RBI repo rate?
```

---

# Deployment

The application is deployed using **Streamlit Cloud**.

Live Deployment:

https://regulatory-knowledge-assistant-rka-q2q7paevuqr2lqvakz7hx9.streamlit.app/

---

# Future Improvements

* Persistent vector database storage
* Advanced document chunking
* Better citation tracking
* Multi-document summarization
* Role-based enterprise deployment

---

# License

MIT License
