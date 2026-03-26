from flask import Blueprint, request, jsonify
from app.services import jogo_service

jogos_bp = Blueprint('jogos', __name__)


@jogos_bp.route('/jogos', methods=['GET'])
def listar_jogos():
    try:
        jogos = jogo_service.listar_jogos()
        return jsonify(jogos), 200
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor'}), 500


@jogos_bp.route('/jogos/<int:jogo_id>', methods=['GET'])
def buscar_jogo(jogo_id):
    try:
        jogo = jogo_service.buscar_jogo(jogo_id)
        return jsonify(jogo), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 404
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor'}), 500


@jogos_bp.route('/jogos', methods=['POST'])
def inserir_jogo():
    try:
        dados = request.get_json()
        jogo = jogo_service.criar_jogo(dados)
        return jsonify(jogo), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor'}), 500


@jogos_bp.route('/jogos/<int:jogo_id>', methods=['PUT'])
def atualizar_jogo(jogo_id):
    try:
        dados = request.get_json()
        jogo_service.atualizar_jogo(jogo_id, dados)
        return '', 204
    except ValueError as e:
        return jsonify({'erro': str(e)}), 404
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor'}), 500


@jogos_bp.route('/jogos/<int:jogo_id>', methods=['DELETE'])
def deletar_jogo(jogo_id):
    try:
        nome = jogo_service.remover_jogo(jogo_id)
        return jsonify({'mensagem': f"Jogo '{nome}' removido"}), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 404
    except Exception:
        return jsonify({'erro': 'Erro interno no servidor'}), 500