from app.extensions import db

# Tabela associativa jogo_plataforma — não é um Model completo,
# é só uma tabela intermediária que o SQLAlchemy gerencia automaticamente
jogo_plataforma = db.Table(
    'jogo_plataforma',
    db.Column('jogo_id',      db.Integer, db.ForeignKey('jogos.id'),      primary_key=True),
    db.Column('plataforma_id', db.Integer, db.ForeignKey('plataformas.id'), primary_key=True)
)


class Plataforma(db.Model):
    __tablename__ = 'plataformas'

    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.Text, nullable=False, unique=True)