import sqlite3

DATABASE = "phishinsight.db"


def get_db():
    return sqlite3.connect(DATABASE)

def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            threat_level TEXT,
            risk_score INTEGER,
            confidence INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()
    db.close()