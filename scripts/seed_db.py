from app import create_app
from app.extensions import db
from app.models.jogo import Jogo
from app.models.plataforma import Plataforma

jogos_data = [
    {
        'nome': 'Bloodborne', 'ano_lancamento': 2015,
        'descricao': 'RPG de ação com ambientação gótica e sombria.',
        'desenvolvedora': 'FromSoftware', 'genero': 'RPG',
        'preco': 99.9, 'quantidade': 5,
        'plataformas': ['PS4', 'PS5']
    },
    {
        'nome': 'Horizon Forbidden West', 'ano_lancamento': 2022,
        'descricao': 'Ação e aventura em mundo aberto pós-apocalíptico.',
        'desenvolvedora': 'Guerrilla', 'genero': 'Ação',
        'preco': 299.9, 'quantidade': 8,
        'plataformas': ['PS4', 'PS5']
    },
    {
        'nome': 'Ghost of Tsushima', 'ano_lancamento': 2020,
        'descricao': 'Aventura em mundo aberto no Japão feudal.',
        'desenvolvedora': 'Sucker Punch', 'genero': 'Ação',
        'preco': 249.9, 'quantidade': 6,
        'plataformas': ['PS4', 'PS5']
    },
    {
        'nome': 'FIFA 23', 'ano_lancamento': 2023,
        'descricao': 'Simulador de futebol realista.',
        'desenvolvedora': 'EA Sports', 'genero': 'Esporte',
        'preco': 199.9, 'quantidade': 10,
        'plataformas': ['PS4', 'PS5', 'PC', 'Xbox One', 'Xbox Series X']
    },
]


def seed():
    app = create_app()
    with app.app_context():
        for dados in jogos_data:
            if Jogo.query.filter_by(nome=dados['nome']).first():
                continue

            jogo = Jogo(
                nome           = dados['nome'],
                ano_lancamento = dados['ano_lancamento'],
                descricao      = dados['descricao'],
                desenvolvedora = dados['desenvolvedora'],
                genero         = dados['genero'],
                preco          = dados['preco'],
                quantidade     = dados['quantidade'],
            )
            db.session.add(jogo)
            db.session.flush()

            for nome in dados['plataformas']:
                plataforma = Plataforma.query.filter_by(nome=nome).first()
                if plataforma is None:
                    plataforma = Plataforma(nome=nome)
                    db.session.add(plataforma)
                    db.session.flush()
                jogo.plataformas.append(plataforma)

        db.session.commit()
        print("Banco populado com sucesso!")


if __name__ == '__main__':
    seed()