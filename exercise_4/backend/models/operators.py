from database import db

# Modelo que representa a tabela 'operadoras' no banco de dados
class Operadora(db.Model):
    __tablename__ = 'operadoras'  # Define o nome da tabela no banco

    # Coluna que representa o número de registro da operadora na ANS (chave primária)
    registro_ans = db.Column(db.Integer, primary_key=True)

    # CNPJ da operadora
    cnpj = db.Column(db.String(20))

    # Razão social da empresa (nome legal registrado)
    razao_social = db.Column(db.String(255))

    # Nome fantasia da operadora (nome pelo qual é conhecida publicamente)
    nome_fantasia = db.Column(db.String(255))

    # Modalidade da operadora (ex: medicina de grupo, cooperativa, etc.)
    modalidade = db.Column(db.String(100))

    # Endereço da sede
    logradouro = db.Column(db.String(255))       # Rua/Avenida
    numero = db.Column(db.String(20))            # Número
    complemento = db.Column(db.String(100))      # Complemento (ex: sala, bloco)
    bairro = db.Column(db.String(100))           # Bairro
    cidade = db.Column(db.String(100))           # Cidade
    uf = db.Column(db.String(2))                 # Unidade federativa (estado)
    cep = db.Column(db.String(10))               # CEP

    # Contatos da operadora
    ddd = db.Column(db.String(5))                # DDD do telefone
    telefone = db.Column(db.String(20))          # Número de telefone
    fax = db.Column(db.String(20))               # Fax (caso exista)
    endereco_eletronico = db.Column(db.String(100))  # E-mail ou outro meio eletrônico

    # Representante legal e seu cargo
    representante = db.Column(db.String(100))
    cargo_representante = db.Column(db.String(100))

    # Região de comercialização dos planos de saúde da operadora
    regiao_de_comercializacao = db.Column(db.Integer)

    # Data em que a operadora foi registrada na ANS
    data_registro_ans = db.Column(db.Date)
