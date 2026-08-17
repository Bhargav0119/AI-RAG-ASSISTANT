from app.services.retrieval_service import retrieve_relevant_chunks

question = "What Python topics are coverd in Week 3?"

results = retrieve_relevant_chunks(question)

print("Retrieved results:")

for match in results["matches"]:
    print("\n--- Result ---")
    print(f"Score: {match['score']}")
    print(f"Chunk: {match['metadata']['chunk']}")
    print(f"Text: {match['metadata']['text']}")