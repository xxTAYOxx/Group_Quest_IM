"""SQLite connection + schema initialization for ListMate."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT / "listmate.db"
SCHEMA_PATH = ROOT / "schema.sql"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    schema = SCHEMA_PATH.read_text()
    with get_conn() as conn:
        conn.executescript(schema)
