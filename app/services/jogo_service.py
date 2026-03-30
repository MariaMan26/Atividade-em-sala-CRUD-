from app.extensions import db
from app.repositories import jogo_repository as repo

CAMPOS_OBRIGATORIOS = ['nome', 'preco', 'quantidade']


def listar_jogos() -> list[dict]:
    try:
        return [jogo.to_dict() for jogo in repo.buscar_todos()]
    except Exception as e:
        raise Exception(f'Erro ao listar jogos: {e}')


def buscar_jogo(jogo_id: int) -> dict:
    try:
        jogo = repo.buscar_por_id(jogo_id)
        if jogo is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        return jogo.to_dict()
    except ValueError:
        raise
    except Exception as e:
        raise Exception(f'Erro ao buscar jogo: {e}')


def criar_jogo(dados: dict) -> dict:
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in dados:
            raise ValueError(f'Campo obrigatório ausente: {campo}')
    try:
        jogo = repo.inserir(dados)
        if 'plataformas' in dados:
            repo.sincronizar_plataformas(jogo, dados['plataformas'])
        db.session.commit()
        return jogo.to_dict()
    except ValueError:
        raise
    except Exception as e:
        db.session.rollback()
        raise Exception(f'Erro ao criar jogo: {e}')


def atualizar_jogo(jogo_id: int, dados: dict) -> None:
    try:
        jogo = repo.buscar_por_id(jogo_id)
        if jogo is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        repo.atualizar(jogo, dados)
        if 'plataformas' in dados:
            repo.sincronizar_plataformas(jogo, dados['plataformas'])
        db.session.commit()
    except ValueError:
        raise
    except Exception as e:
        db.session.rollback()
        raise Exception(f'Erro ao atualizar jogo: {e}')


def remover_jogo(jogo_id: int) -> str:
    try:
        jogo = repo.buscar_por_id(jogo_id)
        if jogo is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        nome = jogo.nome
        repo.deletar(jogo)
        db.session.commit()
        return nome
    except ValueError:
        raise
    except Exception as e:
        db.session.rollback()
        raise Exception(f'Erro ao remover jogo: {e}')