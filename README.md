# AI RAG Assistant

AI RAG Assistant is a Retrieval-Augmented Generation (RAG) application built using Python and FastAPI.

The application extracts text from a PDF document, splits the text into smaller chunks, generates vector embeddings using EmbeddingGemma, stores the embeddings in Pinecone, retrieves relevant document chunks based on a user's question, and uses Llama 3.2 to generate an answer based on the retrieved context.

## Technology Stack

- Python
- FastAPI
- Ollama
- Llama 3.2
- EmbeddingGemma
- Pinecone
- Retrieval-Augmented Generation (RAG)

## Current Architecture

User Question
→ FastAPI `/chat`
→ EmbeddingGemma
→ Pinecone Semantic Search
→ Relevant PDF Chunks
→ Llama 3.2
→ Final Answer

## Project Structure

```text
AI-RAG-Assistant/
│
├── app/
│   ├── api/
│   │   └── chat.py
│   │
│   ├── models/
│   │   └── chat_models.py
│   │
│   └── services/
│       ├── chat_service.py
│       ├── pdf_service.py
│       ├── chunking_service.py
│       ├── embedding_services.py
│       ├── pinecone_service.py
│       ├── vector_service.py
│       ├── retrieval_service.py
│       └── rag_service.py
│
├── data/
│   ├── uploads/
│   └── processed/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Service Responsibilities

- `pdf_service.py` — Extracts text from PDF documents.
- `chunking_service.py` — Splits extracted text into smaller overlapping chunks.
- `embedding_services.py` — Converts text chunks into vector embeddings using EmbeddingGemma.
- `pinecone_service.py` — Connects the application to the Pinecone vector database and manages the index.
- `vector_service.py` — Uploads document embeddings and metadata to Pinecone.
- `retrieval_service.py` — Converts a user's question into an embedding and retrieves the most relevant document chunks from Pinecone.
- `chat_service.py` — Communicates with Llama 3.2 through Ollama to generate text responses.
- `rag_service.py` — Combines retrieved document context with the user's question and sends it to Llama 3.2.
- `chat.py` — Provides the FastAPI `/chat` endpoint.
- `chat_models.py` — Defines the request and response data models used by the API.
- `main.py` — Creates the FastAPI application and registers the API routes.

## RAG Workflow

The application has two main workflows: document indexing and question answering.

### Document Indexing

```text
PDF Document
     ↓
pdf_service.py
     ↓
Extract Text
     ↓
chunking_service.py
     ↓
Text Chunks
     ↓
embedding_services.py
     ↓
EmbeddingGemma
     ↓
768-Dimensional Embeddings
     ↓
vector_service.py
     ↓
Pinecone
```

### Question Answering

```text
User Question
     ↓
FastAPI /chat
     ↓
rag_service.py
     ↓
retrieval_service.py
     ↓
EmbeddingGemma
     ↓
Question Embedding
     ↓
Pinecone Semantic Search
     ↓
Relevant PDF Chunks
     ↓
rag_service.py
     ↓
chat_service.py
     ↓
Llama 3.2
     ↓
Final Answer
```

## How RAG Works

### 1. Document Processing

The PDF document is placed in the `data/uploads/` directory. The application extracts the text from the PDF and divides it into smaller overlapping chunks.

### 2. Embedding Generation

Each text chunk is converted into a 768-dimensional vector embedding using EmbeddingGemma through Ollama.

### 3. Vector Storage

The generated embeddings are stored in Pinecone together with metadata containing the original text and chunk information.

### 4. Semantic Retrieval

When a user asks a question, the question is also converted into an embedding using EmbeddingGemma.

Pinecone compares the question embedding with the stored document embeddings using semantic similarity search and returns the most relevant document chunks.

### 5. Context Generation

The retrieved chunks are combined to create context for the Large Language Model.

### 6. Response Generation

The context and the user's question are sent to Llama 3.2 through Ollama.

Llama 3.2 generates the final answer based on the retrieved document context.

### 7. API Response

FastAPI returns the generated answer through the `/chat` endpoint.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-RAG-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your Pinecone API key.

```env
PINECONE_API_KEY=your_pinecone_api_key
```

Do not commit the `.env` file to GitHub.

### 5. Install Ollama Models

Make sure Ollama is installed, then pull the required models:

```bash
ollama pull llama3.2
ollama pull embeddinggemma
```

### 6. Add a PDF Document

Place the PDF document to be indexed inside:

```text
data/uploads/
```

### 7. Process and Upload the Document

Run:

```bash
python test_vector.py
```

This extracts the PDF text, creates chunks, generates embeddings, and uploads the vectors to Pinecone.

### 8. Start the FastAPI Application

```bash
python -m uvicorn main:app --reload
```

### 9. Test the API

Open the FastAPI Swagger documentation in your browser:

```text
http://127.0.0.1:8000/docs
```

Use the `POST /chat` endpoint with a request such as:

```json
{
  "question": "What Python topics are covered in Week 3?"
}
```

The application retrieves relevant document chunks from Pinecone and uses Llama 3.2 to generate the final answer.

## Current Limitations and Future Improvements

This is Version 1 of the AI RAG Assistant and focuses on implementing the core RAG workflow.

Current limitations and planned improvements include:

- Improve text chunking to preserve document sections and semantic boundaries.
- Improve retrieval accuracy and relevance.
- Add similarity-score filtering for retrieved chunks.
- Add a dedicated document upload and indexing API.
- Support multiple PDF documents.
- Add document and source metadata to responses.
- Add error handling and logging.
- Add automated unit and integration tests.
- Improve configuration management.
- Containerize the application using Docker.
- Explore LangChain or LlamaIndex in a future version.