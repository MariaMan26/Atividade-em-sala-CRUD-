from app.extensions import db
from app.models.jogo import Jogo
from app.models.plataforma import Plataforma


def buscar_todos() -> list[Jogo]:
    return Jogo.query.all()


def buscar_por_id(jogo_id: int) -> Jogo | None:
    return Jogo.query.get(jogo_id)


def inserir(dados: dict) -> Jogo:
    jogo = Jogo(
        nome           = dados['nome'],
        ano_lancamento = dados.get('ano_lancamento'),
        descricao      = dados.get('descricao'),
        desenvolvedora = dados.get('desenvolvedora'),
        genero         = dados.get('genero'),
        preco          = dados['preco'],
        quantidade     = dados['quantidade'],
    )
    db.session.add(jogo)
    db.session.flush()  # gera o ID sem fazer commit ainda
    return jogo


def atualizar(jogo: Jogo, dados: dict) -> Jogo:
    jogo.nome           = dados.get('nome',           jogo.nome)
    jogo.ano_lancamento = dados.get('ano_lancamento', jogo.ano_lancamento)
    jogo.descricao      = dados.get('descricao',      jogo.descricao)
    jogo.desenvolvedora = dados.get('desenvolvedora', jogo.desenvolvedora)
    jogo.genero         = dados.get('genero',         jogo.genero)
    jogo.preco          = dados.get('preco',          jogo.preco)
    jogo.quantidade     = dados.get('quantidade',     jogo.quantidade)
    return jogo


def deletar(jogo: Jogo) -> None:
    db.session.delete(jogo)


def sincronizar_plataformas(jogo: Jogo, nomes: list[str]) -> None:
    plataformas = []
    for nome in nomes:
        plataforma = Plataforma.query.filter_by(nome=nome).first()
        if plataforma is None:
            plataforma = Plataforma(nome=nome)
            db.session.add(plataforma)
            db.session.flush()
        plataformas.append(plataforma)
    jogo.plataformas = plataformas