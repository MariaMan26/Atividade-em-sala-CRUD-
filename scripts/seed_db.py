from app.db.connection import get_conn


def main():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        popular_tabelas(cursor)
        conn.commit()
        print("Banco populado com sucesso!")
    except Exception as e:
        conn.rollback()
        print(f"Erro: {e}")
    finally:
        conn.close()


def popular_tabelas(cursor):
    cursor.execute("""
    INSERT OR IGNORE INTO plataformas (nome) VALUES
    ('PS4'), ('PS5'), ('PC'), ('Xbox One'), ('Xbox Series X')
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO jogos (nome, ano_lancamento, descricao, desenvolvedora, genero, preco, quantidade) VALUES
    ('Bloodborne', 2015, 'RPG de ação com ambientação gótica e sombria.', 'FromSoftware', 'RPG', 99.9, 5),
    ('Horizon Forbidden West', 2022, 'Ação e aventura em mundo aberto pós-apocalíptico.', 'Guerrilla', 'Ação', 299.9, 8),
    ('Ghost of Tsushima', 2020, 'Aventura em mundo aberto no Japão feudal.', 'Sucker Punch', 'Ação', 249.9, 6),
    ('FIFA 23', 2023, 'Simulador de futebol realista.', 'EA Sports', 'Esporte', 199.9, 10)
    """)

    cursor.execute("SELECT nome, id FROM plataformas")
    plataformas = dict(cursor.fetchall())

    cursor.execute("SELECT nome, id FROM jogos")
    jogos = dict(cursor.fetchall())

    relacionamentos = [
        ("Bloodborne",             "PS4"),
        ("Bloodborne",             "PS5"),
        ("Horizon Forbidden West", "PS4"),
        ("Horizon Forbidden West", "PS5"),
        ("Ghost of Tsushima",      "PS4"),
        ("Ghost of Tsushima",      "PS5"),
        ("FIFA 23",                "PS4"),
        ("FIFA 23",                "PS5"),
        ("FIFA 23",                "PC"),
        ("FIFA 23",                "Xbox One"),
        ("FIFA 23",                "Xbox Series X"),
    ]

    for jogo, plataforma in relacionamentos:
        cursor.execute(
            "INSERT OR IGNORE INTO jogo_plataforma VALUES (?, ?)",
            (jogos[jogo], plataformas[plataforma])
        )


if __name__ == "__main__":
    main()