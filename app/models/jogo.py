from app.extensions import db
from app.models.plataforma import jogo_plataforma


class Jogo(db.Model):
    __tablename__ = 'jogos'

    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome           = db.Column(db.Text,    nullable=False)
    ano_lancamento = db.Column(db.Integer)
    descricao      = db.Column(db.Text)
    desenvolvedora = db.Column(db.Text)
    genero         = db.Column(db.Text)
    preco          = db.Column(db.Float,   nullable=False)
    quantidade     = db.Column(db.Integer, nullable=False)

    plataformas = db.relationship(
        'Plataforma',
        secondary=jogo_plataforma,
        lazy='joined'
    )

    def to_dict(self) -> dict:
        return {
            'id':             self.id,
            'nome':           self.nome,
            'ano_lancamento': self.ano_lancamento,
            'descricao':      self.descricao,
            'desenvolvedora': self.desenvolvedora,
            'genero':         self.genero,
            'preco':          self.preco,
            'quantidade':     self.quantidade,
            'plataformas':    [p.nome for p in self.plataformas]
        }