import uuid

from app.db.database import get_cursor

from app.services.embedding_service import (
    generate_embedding
)


def store_chunks(
    chunks,
    document_id,
    filename,
    owner_id
):

    with get_cursor() as cur:
        for chunk in chunks:

            embedding = generate_embedding(
                chunk["chunk_text"]
            )

            cur.execute("""
                INSERT INTO chunks (
                    id,
                    document_id,
                    filename,
                    chunk_text,
                    page_number,
                    embedding,
                    owner_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                str(uuid.uuid4()),
                document_id,
                filename,
                chunk["chunk_text"],
                chunk["page_number"],
                embedding,
                owner_id
            ))
