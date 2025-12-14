import sqlite3
from pathlib import Path

DB_PATH = Path("../database") / "intelligence_platform.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user'
);

CREATE TABLE IF NOT EXISTS cyber_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    i_date TEXT,
    i_type TEXT,
    status TEXT,
    description TEXT,
    reported_by TEXT
);

CREATE TABLE IF NOT EXISTS datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rows INTEGER,
    columns INTEGER,
    uploaded_by TEXT,
    date TEXT
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    priority TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'open',
    created_at TEXT,
    created_date TEXT
);
""")

conn.commit()
conn.close()
