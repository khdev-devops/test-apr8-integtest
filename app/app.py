from flask import Flask, request
import sqlite3
from datetime import datetime, timezone

def create_app(db_connection_string):
    app = Flask(__name__)

    def get_db_connection():
        return sqlite3.connect(db_connection_string)

    def init_db():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @app.route("/", methods=["GET"])
    def home():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, text, timestamp FROM notes")
        notes = cur.fetchall()
        conn.close()
        return "<br>".join([f"{n[0]}: {n[1]} ({n[2]})" for n in notes])

    @app.route("/note", methods=["POST"])
    def add_note():
        text = request.json.get("text", "")
        if not text:
            return "Missing text", 400
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO notes (text, timestamp) VALUES (?, ?)", (text, datetime.now(timezone.utc).isoformat()))
        conn.commit()
        conn.close()
        return "Note added", 201

    # Lägg till init som en metod på app-objektet för test
    app.init_db = init_db

    return app