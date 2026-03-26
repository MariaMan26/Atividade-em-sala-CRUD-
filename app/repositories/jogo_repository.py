import sqlite3

_CAMPOS = ['nome', 'ano_lancamento', 'descricao', 'desenvolvedora', 'genero', 'preco', 'quantidade']

_SELECT_JOGO = """
    SELECT j.*, GROUP_CONCAT(p.nome) as plataformas
    FROM jogos j
    LEFT JOIN jogo_plataforma jp ON j.id = jp.jogo_id
    LEFT JOIN plataformas p ON jp.plataforma_id = p.id
"""


def buscar_todos(cursor: sqlite3.Cursor) -> list[dict]:
    cursor.execute(f"{_SELECT_JOGO} GROUP BY j.id")
    return [dict(row) for row in cursor.fetchall()]


def buscar_por_id(cursor: sqlite3.Cursor, jogo_id: int) -> dict | None:
    cursor.execute(f"{_SELECT_JOGO} WHERE j.id = ? GROUP BY j.id", (jogo_id,))
    row = cursor.fetchone()
    return dict(row) if row else None


def inserir(cursor: sqlite3.Cursor, dados: dict) -> int:
    campos = ', '.join(_CAMPOS)
    placeholders = ', '.join(f':{c}' for c in _CAMPOS)
    cursor.execute(
        f"INSERT INTO jogos ({campos}) VALUES ({placeholders})",
        {campo: dados.get(campo) for campo in _CAMPOS}
    )
    return cursor.lastrowid


def atualizar(cursor: sqlite3.Cursor, jogo_id: int, dados: dict, jogo_atual: dict) -> None:
    set_clause = ', '.join(f'{c} = :{c}' for c in _CAMPOS)
    params = {campo: dados.get(campo, jogo_atual[campo]) for campo in _CAMPOS}
    params['id'] = jogo_id
    cursor.execute(f"UPDATE jogos SET {set_clause} WHERE id = :id", params)


def deletar(cursor: sqlite3.Cursor, jogo_id: int) -> None:
    cursor.execute("DELETE FROM jogo_plataforma WHERE jogo_id = ?", (jogo_id,))
    cursor.execute("DELETE FROM jogos WHERE id = ?", (jogo_id,))


def sincronizar_plataformas(cursor: sqlite3.Cursor, jogo_id: int, nomes: list[str]) -> None:
    cursor.execute("DELETE FROM jogo_plataforma WHERE jogo_id = ?", (jogo_id,))
    for nome in nomes:
        cursor.execute("INSERT OR IGNORE INTO plataformas (nome) VALUES (?)", (nome,))
        cursor.execute("SELECT id FROM plataformas WHERE nome = ?", (nome,))
        plataforma_id = cursor.fetchone()[0]
        cursor.execute("INSERT OR IGNORE INTO jogo_plataforma VALUES (?, ?)", (jogo_id, plataforma_id))