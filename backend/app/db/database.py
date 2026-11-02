import os
from contextlib import contextmanager
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(
    dotenv_path=ENV_PATH,
    override=True
)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is required")


def get_connection():
    return psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )


@contextmanager
def get_cursor():
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:
                yield cur
    finally:
        conn.close()
