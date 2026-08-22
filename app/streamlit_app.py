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
        ["Chat", "Upload PDFs", "Evaluation", "About"],
        index=0
    )
    
    if mode == "About":
        st.info("""
        **RBI Circular RAG System**
        
        An open-source Retrieval-Augmented Generation system that:
        - Indexes RBI regulatory circulars
        - Answers compliance queries with citations
        - Uses hybrid BM25 + vector search
        - Powered by Groq Llama 3.3 70B
        
        **Version:** 1.0.0
        """)

# Main content
if mode == "Chat":
    st.subheader("💬 Query Assistant")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_query = st.text_input(
            "Ask a question about RBI regulations:",
            placeholder="E.g., What are KYC requirements?"
        )
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    if search_button and user_query:
        with st.spinner("Searching RBI circulars..."):
            st.info("""
            **Note:** This is a demo interface. 
            
            To use the full RAG pipeline:
            1. Download RBI circulars: `python crawl/pdf_downloader.py --limit 21`
            2. Ingest into ChromaDB: `python scripts/run_ingestion.py --skip-crawl`
            3. The search will then return real answers with citations
            """)
    
    st.markdown("---")
    
    # Display sample results
    st.subheader("📚 How It Works")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1️⃣ Retrieval
        - BM25 keyword search
        - Vector similarity search
        - Hybrid ranking
        """)
    
    with col2:
        st.markdown("""
        ### 2️⃣ Reranking
        - LLM-based relevance scoring
        - Cross-encoder selection
        - Top results filtering
        """)
    
    with col3:
        st.markdown("""
        ### 3️⃣ Generation
        - Groq Llama 3.3 70B
        - Context-aware response
        - Source citations
        """)

elif mode == "Upload PDFs":
    st.subheader("📤 Upload RBI Circulars")
    
    st.info("""
    **Note:** This interface is for demonstration.
    
    To ingest PDFs:
    1. Place PDFs in `data/pdfs/`
    2. Run: `python scripts/run_ingestion.py --skip-crawl`
    3. Vector embeddings will be stored in `data/chroma_db/`
    """)
    
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type="pdf",
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.success(f"Ready to ingest {len(uploaded_files)} files")
        st.warning("Run `python scripts/run_ingestion.py` to process them")

elif mode == "Evaluation":
    st.subheader("📊 RAGAS Evaluation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Context Precision", "1.000", "+100%")
        st.metric("Faithfulness", "0.500", "±0%")
    
    with col2:
        st.metric("Context Recall", "0.639", "+64%")
        st.metric("Answer Relevancy", "0.366", "+37%")
    
    st.info("""
    **Evaluation Details:**
    - Dataset: 7 dev-split questions (20 total)
    - Judge Model: Mistral 7B
    - Embedding: BAAI/bge-small-en-v1.5
    - Chunk Size: 1400
    
    Run evaluation: `python eval/ragas_eval.py --mode rag --split dev --save`
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏦 RBI Circular RAG System | <a href='https://github.com/SAHILARORA0010/rbi-rag'>GitHub</a></p>
    <p><small>Educational and research use only. Always refer to official RBI circulars.</small></p>
</div>
""", unsafe_allow_html=True)
