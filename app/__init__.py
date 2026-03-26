from flask import Flask
from app.db.init_db import criar_banco
from app.routes.jogos import jogos_bp
from app.routes.main import main_bp


def create_app():
    app = Flask(__name__)

    criar_banco()

    app.register_blueprint(jogos_bp, url_prefix='/api')
    app.register_blueprint(main_bp)

    return app