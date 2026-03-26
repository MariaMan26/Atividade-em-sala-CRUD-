from app.db.connection import get_conn
from app.repositories import jogo_repository as repo

CAMPOS_OBRIGATORIOS = ['nome', 'preco', 'quantidade']


def _formatar(jogo: dict) -> dict:
    """Transforma a string de plataformas do GROUP_CONCAT em lista."""
    jogo['plataformas'] = jogo['plataformas'].split(',') if jogo['plataformas'] else []
    return jogo


def listar_jogos() -> list[dict]:
    conn = get_conn()
    try:
        return [_formatar(jogo) for jogo in repo.buscar_todos(conn.cursor())]
    except Exception as e:
        raise Exception(f'Erro ao listar jogos: {e}')
    finally:
        conn.close()


def buscar_jogo(jogo_id: int) -> dict:
    conn = get_conn()
    try:
        jogo = repo.buscar_por_id(conn.cursor(), jogo_id)
        if jogo is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        return _formatar(jogo)
    except ValueError:
        raise
    except Exception as e:
        raise Exception(f'Erro ao buscar jogo: {e}')
    finally:
        conn.close()


def criar_jogo(dados: dict) -> dict:
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in dados:
            raise ValueError(f'Campo obrigatório ausente: {campo}')

    conn = get_conn()
    try:
        cursor = conn.cursor()
        jogo_id = repo.inserir(cursor, dados)
        if 'plataformas' in dados:
            repo.sincronizar_plataformas(cursor, jogo_id, dados['plataformas'])
        conn.commit()
        return _formatar(repo.buscar_por_id(conn.cursor(), jogo_id))
    except ValueError:
        raise
    except Exception as e:
        conn.rollback()
        raise Exception(f'Erro ao criar jogo: {e}')
    finally:
        conn.close()


def atualizar_jogo(jogo_id: int, dados: dict) -> None:
    conn = get_conn()
    try:
        cursor = conn.cursor()
        jogo_atual = repo.buscar_por_id(cursor, jogo_id)
        if jogo_atual is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        repo.atualizar(cursor, jogo_id, dados, jogo_atual)
        if 'plataformas' in dados:
            repo.sincronizar_plataformas(cursor, jogo_id, dados['plataformas'])
        conn.commit()
    except ValueError:
        raise
    except Exception as e:
        conn.rollback()
        raise Exception(f'Erro ao atualizar jogo: {e}')
    finally:
        conn.close()


def remover_jogo(jogo_id: int) -> str:
    conn = get_conn()
    try:
        cursor = conn.cursor()
        jogo = repo.buscar_por_id(cursor, jogo_id)
        if jogo is None:
            raise ValueError(f'Jogo {jogo_id} não encontrado')
        repo.deletar(cursor, jogo_id)
        conn.commit()
        return jogo['nome']
    except ValueError:
        raise
    except Exception as e:
        conn.rollback()
        raise Exception(f'Erro ao remover jogo: {e}')
    finally:
        conn.close()