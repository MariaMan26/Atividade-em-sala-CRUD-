from app.db.connection import get_conn

def criar_banco():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano_lancamento INTEGER,
        descricao TEXT,
        desenvolvedora TEXT,
        genero TEXT,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plataformas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogo_plataforma (
        jogo_id INTEGER,
        plataforma_id INTEGER,
        PRIMARY KEY (jogo_id, plataforma_id),
        FOREIGN KEY (jogo_id) REFERENCES jogos(id),
        FOREIGN KEY (plataforma_id) REFERENCES plataformas(id)
    )
    """)

    conn.commit()
    conn.close()