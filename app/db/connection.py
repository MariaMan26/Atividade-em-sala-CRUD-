import sqlite3
import os

DB_PATH = os.path.join('instance', 'inventario_jogos.db')

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn