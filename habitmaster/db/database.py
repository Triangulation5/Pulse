import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "habits.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT,
                description TEXT,
                remind BOOLEAN DEFAULT FALSE,
                archived BOOLEAN DEFAULT FALSE
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT CHECK(status IN ('completed', 'missed')) NOT NULL,
                FOREIGN KEY(habit_id) REFERENCES habits(id) ON DELETE CASCADE,
                UNIQUE(habit_id, date)
            )
        """)
        conn.commit()


def add_habit(name, category=None, description=None):
    with get_connection() as conn:
        conn.execute("INSERT INTO habits (name, category, description) VALUES (?, ?, ?)", (name, category, description))
        conn.commit()


def delete_habit(name):
    with get_connection() as conn:
        conn.execute("DELETE FROM habits WHERE name = ?", (name,))
        conn.commit()


def rename_habit(old_name, new_name):
    with get_connection() as conn:
        conn.execute("UPDATE habits SET name = ? WHERE name = ?", (new_name, old_name))
        conn.commit()


def list_habits(include_archived=False):
    with get_connection() as conn:
        query = "SELECT * FROM habits"
        if not include_archived:
            query += " WHERE archived = FALSE"
        query += " ORDER BY name"
        cur = conn.execute(query)
        return cur.fetchall()


def log_status(habit_name, date_str, status):
    with get_connection() as conn:
        cur = conn.execute("SELECT id FROM habits WHERE name = ?", (habit_name,))
        row = cur.fetchone()
        if not row:
            raise ValueError(f"Habit '{habit_name}' not found.")
        habit_id = row["id"]
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        conn.execute(
            """
            INSERT OR REPLACE INTO logs (habit_id, date, status)
            VALUES (?, ?, ?)
        """,
            (habit_id, date_str, status),
        )
        conn.commit()


def get_logs(habit_name, start=None, end=None):
    with get_connection() as conn:
        cur = conn.execute("SELECT id FROM habits WHERE name = ?", (habit_name,))
        row = cur.fetchone()
        if not row:
            raise ValueError(f"Habit '{habit_name}' not found.")
        habit_id = row["id"]
        query = "SELECT date, status FROM logs WHERE habit_id = ?"
        params = [habit_id]
        if start:
            query += " AND date >= ?"
            params.append(start)
        if end:
            query += " AND date <= ?"
            params.append(end)
        cur = conn.execute(query, tuple(params))
        return {row["date"]: row["status"] for row in cur.fetchall()}


def set_habit_attribute(name, attribute, value):
    with get_connection() as conn:
        conn.execute(f"UPDATE habits SET {attribute} = ? WHERE name = ?", (value, name))
        conn.commit()

def get_habit(name):
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM habits WHERE name = ?", (name,))
        return cur.fetchone()
