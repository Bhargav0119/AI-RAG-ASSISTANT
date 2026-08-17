from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import split_text

pdf_path = "data/uploads/python_basics.pdf"

text = extract_text_from_pdf(pdf_path)

print(f"Total characters extracted: {len(text)}")

chunks = split_text(text)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)