import os
import pandas as pd
from flask_cors import CORS
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database import db
from models.operators import Operadora
from sqlalchemy import text, or_
import time

# Carrega variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Inicializa o app Flask
server = Flask(__name__)
CORS(server)  # Permite requisições de diferentes origens (Cross-Origin Resource Sharing)

# Recupera credenciais do banco a partir do .env
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
env = os.getenv('ENV')

# Configura a URI de conexão com o banco de dados MySQL
server.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{dbname}'

# Inicializa a extensão SQLAlchemy com o app Flask
db.init_app(server)

# Tenta se conectar ao banco repetidamente até ele estar disponível
for _ in range(10):
    try:
        with db.engine_check.connect() as conn:
            result = conn.execute(text("SHOW DATABASES LIKE 'ans_database'"))
            if result.first():
                break
        print("Aguardando criação do banco...")
    except:
        pass
    time.sleep(3)

# Cria as tabelas do banco e importa os dados do CSV caso a tabela esteja vazia
with server.app_context():
    db.create_all()
    if not Operadora.query.first():
        print("Importando CSV...")
        df = pd.read_csv("data/ANS/Relatorio_cadop.csv", sep=";", encoding="utf-8",  header=0)
        df.to_sql("operadoras", con=db.engine, if_exists="append", index=False)
        print("Dados importados.")

# Rota de busca com paginação e filtro por nome, razão social ou CNPJ
@server.route('/search', methods=['GET'])
def search_operators():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))       
    per_page = int(request.args.get('per_page', 10))  

    # Retorna resultado vazio caso nenhum termo de busca seja fornecido
    if not query:
        return jsonify({
            "total": 0,
            "page": page,
            "per_page": per_page,
            "results": []
        })
    
    # Realiza consulta no banco usando filtros parciais (ilike = case insensitive)
    pagination = Operadora.query.filter(
        or_(
            Operadora.nome_fantasia.ilike(f"%{query}%"),
            Operadora.razao_social.ilike(f"%{query}%"),
            Operadora.cnpj.ilike(f"%{query}%"),
        )
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    # Monta os dados a serem retornados em formato JSON
    operators = []
    for op in pagination.items:
        operators.append({
            "nome_fantasia": op.nome_fantasia,
            "registro_ans": op.registro_ans,
            "cnpj": op.cnpj,
            "telefone": op.telefone,
            "endereco_eletronico": op.endereco_eletronico,
            "razao_social": op.razao_social
        })

    # Retorna os resultados da busca paginada
    return jsonify({
        "total": pagination.total,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "pages": pagination.pages,
        "results": operators
    })

# Rota simples de verificação de saúde da API
@server.route("/health")
def index():
    return jsonify({"status": "Ok!"})

# Rota de teste de conexão com o banco de dados
@server.route("/test-db")
def test_db():
    try:
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return '✅ Connection to the database was successful!'
    except Exception as e:
        return f"Database connection failed: {str(e)}"

# Inicia o servidor Flask
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)
