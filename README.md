# Retrievium – Production RAG Platform

## Overview

Retrievium is a production-oriented Retrieval-Augmented Generation (RAG) platform that enables users to upload documents, perform semantic search, and receive context-aware AI-generated responses.

The system combines modern retrieval techniques, vector databases, secure authentication, and per-user document isolation to deliver a scalable knowledge retrieval experience.

Unlike basic RAG demos, Retrievium implements end-to-end document ownership enforcement, ensuring users can only retrieve information from documents they have uploaded themselves.

---

## Architecture

```text
User
 │
 ▼
Next.js Frontend
 │
 ▼
FastAPI Backend
 │
 ├── JWT Authentication
 ├── PDF Processing
 ├── Chunking Pipeline
 ├── Embedding Generation
 ├── Hybrid Retrieval
 └── Response Generation
 │
 ▼
PostgreSQL + pgvector (Supabase)
```

---

## Key Features

### Authentication & Security

- JWT-based authentication
- Secure password hashing
- Protected API endpoints
- User session persistence
- Route-level access control

### Document Processing

- PDF upload support
- Automated text extraction
- Recursive document chunking
- Metadata preservation
- Scalable ingestion pipeline

### Retrieval Pipeline

- OpenAI embedding generation
- pgvector vector storage
- Semantic similarity search
- Hybrid retrieval architecture
- Retrieval reranking
- Context-aware response generation

### Multi-Tenant Isolation

- Per-user document ownership
- Ownership-aware retrieval
- Protected document access
- Secure user-level data separation

### Evaluation & Observability

- Retrieval evaluation utilities
- Relevance testing dataset
- Metrics tracking
- Modular retrieval architecture

---

## Technical Highlights

### Hybrid Retrieval

Retrievium combines:

- Dense vector retrieval
- Lexical relevance matching

This improves retrieval quality compared to traditional vector-only search systems.

### Ownership-Aware Search

Every document chunk is associated with a user identifier.

During retrieval:

```sql
WHERE owner_id = current_user_id
```

This guarantees that users can only access their own document corpus.

### Semantic Search Infrastructure

Embeddings are generated using OpenAI models and stored in PostgreSQL using the pgvector extension.

Similarity search is performed directly inside the database using vector distance operators.

---

## Tech Stack

### Frontend

- Next.js
- React
- TypeScript

### Backend

- FastAPI
- Python

### Database

- PostgreSQL
- pgvector
- Supabase

### AI & Retrieval

- OpenAI Embeddings
- Sentence Transformers
- Hybrid Search
- Semantic Retrieval

### Security

- JWT Authentication
- Password Hashing
- Protected Routes
- User Ownership Enforcement

---

## Project Structure

```text
Retrievium/
│
├── backend/
│   ├── app/
│   │   ├── auth.py
│   │   ├── ingestion/
│   │   ├── retrieval/
│   │   ├── services/
│   │   └── db/
│   │
│   └── evaluation/
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── services/
│
├── docs/
└── infrastructure/
```

---

## Example Workflow

1. User uploads a PDF
2. Text is extracted and chunked
3. Embeddings are generated
4. Chunks are stored in PostgreSQL + pgvector
5. User submits a query
6. Hybrid retrieval finds relevant chunks
7. Context is passed to the LLM
8. Grounded response is generated

---

## Engineering Challenges Solved

- Secure multi-user authentication
- Vector database integration
- Hybrid retrieval implementation
- Per-user document ownership
- End-to-end RAG pipeline orchestration
- Production-oriented API architecture
- Scalable document ingestion workflow

---

## Future Improvements

- Streaming responses
- Conversation memory
- Citation generation
- Advanced reranking models
- Multi-document collections
- Admin analytics dashboard
- Kubernetes deployment
- CI/CD automation

---

Production-grade RAG platform built using FastAPI, Next.js, OpenAI Embeddings, PostgreSQL, pgvector, JWT Authentication, and Hybrid Retrieval.
