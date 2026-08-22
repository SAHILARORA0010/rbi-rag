import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="RBI Circular RAG System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🏦 RBI Circular RAG System")
st.markdown("### Reserve Bank of India Regulatory Query Assistant")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    mode = st.radio(
        "Select Mode:",
        ["Chat", "Setup Guide", "Evaluation", "About"],
        index=0
    )

# Main content
if mode == "Chat":
    st.subheader("💬 Query Assistant")
    
    st.info("""
    ✅ **Demo Interface Ready!**
    
    To enable full RAG functionality:
    
    **Step 1: Install Locally**
    ```bash
    git clone https://github.com/SAHILARORA0010/rbi-rag.git
    cd rbi-rag
    pip install -r requirements.txt
    ```
    
    **Step 2: Setup Data**
    ```bash
    python crawl/pdf_downloader.py --limit 21
    python scripts/run_ingestion.py --skip-crawl
    ```
    
    **Step 3: Run**
    ```bash
    python run.py
    ```
    """)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_query = st.text_input(
            "Ask a question about RBI regulations:",
            placeholder="E.g., What are KYC requirements?"
        )
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    if search_button and user_query:
        st.warning("⚠️ RAG pipeline not active in demo. Run locally to enable.")

elif mode == "Setup Guide":
    st.subheader("📚 Quick Start Guide")
    
    st.markdown("""
    ### 1️⃣ Clone Repository
    ```bash
    git clone https://github.com/SAHILARORA0010/rbi-rag.git
    cd rbi-rag
    ```
    
    ### 2️⃣ Create Virtual Environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\\Scripts\\activate
    ```
    
    ### 3️⃣ Install Dependencies
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    playwright install chromium
    ```
    
    ### 4️⃣ Configure API Keys
    ```bash
    cp .env.example .env
    # Edit .env and add your GROQ_API_KEY
    ```
    
    ### 5️⃣ Download & Ingest RBI Circulars
    ```bash
    python crawl/pdf_downloader.py --limit 21
    python scripts/run_ingestion.py --skip-crawl
    ```
    
    ### 6️⃣ Run the Application
    ```bash
    python run.py
    ```
    
    Open browser to: **http://localhost:8501** 🎉
    """)

elif mode == "Evaluation":
    st.subheader("📊 RAGAS Evaluation Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Context Precision", "1.000", "Perfect")
        st.metric("Faithfulness", "0.500", "Fair")
    
    with col2:
        st.metric("Context Recall", "0.639", "Good")
        st.metric("Answer Relevancy", "0.366", "Developing")
    
    st.info("""
    **Evaluation Configuration:**
    - Model: Mistral 7B (Judge)
    - Dataset: 7 questions (dev split)
    - Embeddings: BAAI/bge-small-en-v1.5
    - Chunk Size: 1400 tokens
    
    **Run Evaluation:**
    ```bash
    python eval/ragas_eval.py --mode rag --split dev --save
    ```
    """)

elif mode == "About":
    st.subheader("ℹ️ About RBI-RAG")
    
    st.markdown("""
    ## 🏦 RBI Circular RAG System
    
    An open-source Retrieval-Augmented Generation system for Reserve Bank of India regulatory compliance.
    
    ### Features
    ✅ Indexes RBI regulatory circulars  
    ✅ Hybrid BM25 + vector search  
    ✅ LLM-powered query rewriting  
    ✅ Source citations & references  
    ✅ Automated evaluation (RAGAS)  
    ✅ GitHub Actions CI/CD  
    
    ### Tech Stack
    - **LLM:** Groq Llama 3.3 70B
    - **Vector DB:** ChromaDB
    - **Embeddings:** Sentence Transformers
    - **Search:** BM25 + Vector Hybrid
    - **UI:** Streamlit
    - **Framework:** LangChain
    
    ### Architecture
    ```
    RBI Circulars → PDF Download → Text Extraction → Chunking
                                        ↓
                                    Embeddings
                                        ↓
                                    ChromaDB
                                        ↓
    User Query → Rewrite → Hybrid Search → Rerank → LLM → Answer + Citations
    ```
    
    ### Repository
    🔗 https://github.com/SAHILARORA0010/rbi-rag
    
    ### Contributors
    - Samrat Chowdhury - RAG Pipeline
    - Nisha Chowdhury - Streamlit UI
    - SAHIL ARORA - CI/CD Automation
    
    ### Disclaimer
    ⚠️ Educational and research use only.  
    Always refer to official RBI circulars for compliance decisions.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏦 RBI Circular RAG System v1.0</p>
    <p><small><a href='https://github.com/SAHILARORA0010/rbi-rag'>GitHub</a> | 
    <a href='https://github.com/SAHILARORA0010/rbi-rag/issues'>Report Issue</a></small></p>
    <p><small>Educational use only. Refer to rbi.org.in for official information.</small></p>
</div>
""", unsafe_allow_html=True)
