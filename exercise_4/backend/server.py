import os
from flask_cors import CORS
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database import db
from models.operators import Operadora
from sqlalchemy import text, or_
load_dotenv()

server = Flask(__name__)
CORS(server)

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')

server.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{dbname}'

db.init_app(server)

@server.route('/search', methods=['GET'])
def search_operators():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))       
    per_page = int(request.args.get('per_page', 10))  

    if(not query):
        return jsonify({
            "total": 0,
            "page": page,
            "per_page": per_page,
            "results": []
        })
    
    pagination = Operadora.query.filter(
        or_(
            Operadora.nome_fantasia.ilike(f"%{query}%"),
            Operadora.razao_social.ilike(f"%{query}%"),
            Operadora.cnpj.ilike(f"%{query}%"),
            
        )
    ).paginate(page=page, per_page=per_page, error_out=False)
    
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
    return jsonify({
        "total": pagination.total,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "pages": pagination.pages,
        "results": operators
    })

@server.route("/health")
def index():
    return jsonify({"status": "Ok!"})

@server.route("/test-db")
def test_db():
    try:
      with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return '✅ Connection to the database was successful!'
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    server.run(debug=True)