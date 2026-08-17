import os

from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE API KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)

INDEX_NAME = "airagassistant"

if not pc.has_index(INDEX_NAME):
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

print(f"Pinecone index '{INDEX_NAME}' is ready.")