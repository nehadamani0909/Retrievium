from app.db.database import cur


SUMMARY_TERMS = (
    "summarize",
    "summary",
    "overview",
    "brief",
    "key points",
    "main points",
    "tl;dr",
    "tldr",
)


def is_summary_query(query: str) -> bool:
    normalized_query = query.lower()

    return any(
        term in normalized_query
        for term in SUMMARY_TERMS
    )


def fetch_document_chunks(
    document_id: str,
    owner_id: str
):
    cur.execute(
        """
        SELECT
            chunk_text,
            page_number,
            filename,
            document_id
        FROM chunks
        WHERE document_id = %s
        AND owner_id = %s
        ORDER BY page_number
        """,
        (
            document_id,
            owner_id
        )
    )

    rows = cur.fetchall()

    return [
        {
            "chunk_text": row[0],
            "page_number": row[1],
            "filename": row[2],
            "document_id": row[3]
        }
        for row in rows
    ]
