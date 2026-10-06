import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "history.db"

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            sender TEXT,
            subject TEXT,
            score INTEGER NOT NULL,
            classification TEXT NOT NULL,
            finding_count INTEGER NOT NULL,
            result_json TEXT NOT NULL
        )
        """)
        conn.commit()

def save_analysis(result, sender, subject):
    payload = json.dumps(result.to_dict(), ensure_ascii=False)
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO analyses(created_at,sender,subject,score,classification,finding_count,result_json) VALUES(?,?,?,?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), sender, subject,
             result.score, result.classification, len(result.findings), payload)
        )
        conn.commit()

def load_history(limit=200):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id,created_at,sender,subject,score,classification,finding_count "
            "FROM analyses ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(r) for r in rows]

def clear_history():
    with get_connection() as conn:
        conn.execute("DELETE FROM analyses")
        conn.commit()
