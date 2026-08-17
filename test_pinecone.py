from app.services.pinecone_service import INDEX_NAME, pc

print("Connected to Pinecone")

print("Indexes:")

for index in pc.list_indexes():
    print(index)
    