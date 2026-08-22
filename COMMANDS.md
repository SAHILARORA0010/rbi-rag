# RBI RAG — Command Reference

Always activate the environment first:
```bash
cd rbi-rag
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## 1. Run the app (RAG UI)
```bash
python run.py
```
Open http://localhost:8501 in browser.

---

## 2. Download RBI Master Circulars (Playwright)
```bash
python crawl/pdf_downloader.py --limit 21
```
Downloads to `data/pdfs/`. Bypasses bot protection using headless browser.
Run this whenever new Master Circulars are published (typically April each year).

---

## 3. Ingest PDFs into ChromaDB
```bash
# After downloading new PDFs:
python scripts/run_ingestion.py --skip-crawl

# Full pipeline (crawl + ingest):
python scripts/run_ingestion.py --limit 50
```

---

## 4. Smoke test the pipeline
```bash
python scripts/test_pipeline.py
```
Fires 5 test queries and shows answers with sources.

---

## 5. Run RAGAS evaluation
```bash
# Dev split (7 questions):
python eval/ragas_eval.py --mode rag --split dev --save

# Full eval (all 20 questions):
python eval/ragas_eval.py --mode rag --split all --save
```
Results saved to `benchmarks/`.

---

## 6. Check what's indexed in ChromaDB
```bash
python -c "
import chromadb
client = chromadb.PersistentClient(path='data/chroma_db')
col = client.get_collection('rbi_circulars')
results = col.get(include=['metadatas'])
print(f'Total chunks: {len(results[\"ids\"])}')
for m in results['metadatas'][:5]:
    print(m.get('circular_no','?'), '|', str(m.get('subject','?'))[:60])
"
```

---

## 7. Check PDF integrity
```bash
python -c "
import fitz
from pathlib import Path
for p in Path('data/pdfs').glob('*.pdf'):
    doc = fitz.open(p)
    text = doc[0].get_text().strip()[:50]
    status = 'OK' if '%PDF' in open(p,'rb').read(4).decode('latin1') else 'STUB'
    print(f'{status} | {p.name} | {doc.page_count} pages')
    doc.close()
"
```

---

## 8. Clear and re-index from scratch
```bash
rm -rf data/chroma_db
python scripts/run_ingestion.py --skip-crawl
```

---

## 9. Git workflow
```bash
git add -A
git commit -m "feat/fix/docs: description"
git push origin main
```

---

## 10. Update requirements after installing new packages
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "chore: update requirements"
git push origin main
```
