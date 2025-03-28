from database import db
class Operadora(db.Model):
    __tablename__ = 'operadoras'

    registro_ans = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20))
    razao_social = db.Column(db.String(255))
    nome_fantasia = db.Column(db.String(255))
    modalidade = db.Column(db.String(100))
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(20))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    cep = db.Column(db.String(10))
    ddd = db.Column(db.String(5))
    telefone = db.Column(db.String(20))
    fax = db.Column(db.String(20))
    endereco_eletronico = db.Column(db.String(100))
    representante = db.Column(db.String(100))
    cargo_representante = db.Column(db.String(100))
    regiao_de_comercializacao = db.Column(db.Integer)
    data_registro_ans = db.Column(db.Date)