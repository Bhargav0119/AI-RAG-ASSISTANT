from app.services.pinecone_service import pc, INDEX_NAME

index = pc.Index(INDEX_NAME)

stats = index.describe_index_stats()

print("Pinecone Index statistics:")
print(stats)