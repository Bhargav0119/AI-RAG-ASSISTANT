from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import split_text
from app.services.embedding_services import generate_embeddings
from app.services.vector_service import upload_vectors


pdf_path = "data/uploads/python_basics.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

embeddings = generate_embeddings(chunks)

uploaded_count = upload_vectors(chunks, embeddings)

print(f"Total chunks: {len(chunks)}")
print(f"Total embeddings: {len(embeddings)}")
print(f"Vectors uploaded: {uploaded_count}")