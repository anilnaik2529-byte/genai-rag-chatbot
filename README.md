# GenAI RAG Assistant

A simple Retrieval-Augmented Generation (RAG) assistant built using FastAPI and TF-IDF vector search.

This system retrieves relevant information from a knowledge base (`docs.json`) and returns the most relevant answers for user queries.

---

# Project Overview

This project demonstrates a basic RAG (Retrieval-Augmented Generation) pipeline.

Instead of generating answers from a large language model alone, the system:

1. Retrieves relevant information from stored documents
2. Uses similarity search to find the best matches
3. Returns the retrieved content as the response

This improves accuracy and ensures answers come from the knowledge base.

---

# Architecture Diagram

```
User Query
   |
   v
FastAPI Backend (/api/chat)
   |
   v
Vector Store (TF-IDF)
   |
   v
Cosine Similarity Search
   |
   v
Top-3 Relevant Chunks Retrieved
   |
   v
Response Returned to User
```

---

# System Workflow

1. User sends a query through the API.
2. FastAPI receives the request.
3. The query is converted into a TF-IDF vector.
4. Cosine similarity is calculated against stored document vectors.
5. Top-3 most relevant chunks are retrieved.
6. Retrieved chunks are returned as the response.

---

# Project Structure

```
genai-rag-assistant
│
├── app.py
├── vector_store.py
├── docs.json
├── requirements.txt
│
├── frontend
│   └── index.html
│
└── README.md
```

---

# File Description

**app.py**

FastAPI backend that exposes the `/api/chat` endpoint.

**vector_store.py**

Handles vectorization, document storage, and similarity search.

**docs.json**

Knowledge base containing text documents.

**requirements.txt**

Python dependencies required to run the project.

**frontend/index.html**

Simple UI for interacting with the API.

**README.md**

Project documentation.

---

# Installation

## Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Server

```
uvicorn app:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides interactive API documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

You can test the API directly from this interface.

---

# API Endpoint

POST

```
/api/chat
```

Example request:

```
{
 "sessionId": "abc123",
 "message": "How can I reset password?"
}
```

---

# Example Response

```
{
 "reply": "Users can reset their password from Settings > Security.",
 "retrievedChunks": 3
}
```

---

# Example Queries

You can test the system using queries like:

* How can I reset password?
* How can I change my email address?
* How do I manage billing settings?

---

# Technologies Used

* Python
* FastAPI
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Uvicorn
* HTML

---

# Future Improvements

Possible improvements to this system:

* Replace TF-IDF with embedding models
* Use FAISS vector database
* Integrate LLMs like OpenAI or Llama
* Add chat history
* Improve frontend UI

---

# Conclusion

This project demonstrates a simple Retrieval-Augmented Generation (RAG) system using FastAPI and vector similarity search.

The system retrieves the most relevant information from the knowledge base and returns it as the response to user queries.
## API Test Screenshot


![alt text](<Screenshot (18).png>)