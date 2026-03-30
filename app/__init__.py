from flask import Flask
from app.extensions import db
from app.routes.jogos import jogos_bp
from app.routes.main import main_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario_jogos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importa os models antes do create_all para o SQLAlchemy reconhecê-los
    from app.models import jogo, plataforma

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(jogos_bp, url_prefix='/api')

    return app