# 🏥 Projeto ANS - Web Scraping + API + Frontend

Este projeto foi desenvolvido como parte de um desafio técnico para uma vaga de estágio. Ele automatiza a extração de informações públicas da ANS (Agência Nacional de Saúde Suplementar), armazena os dados em um banco de dados relacional, expõe esses dados via API e fornece uma interface frontend para consulta e visualização.

---

## 📁 Estrutura do Projeto

```

├── exercise_1/
│   ├── web_scraping.py       # Web scraping dos PDFs da ANS
├── exercise_2/
│   ├── data_transforming.py  # Extração e transformação de dados do PDF
├── exercise_3/
│   ├── 01_create_table_operadoras.sql           # Criação da tabela operadoras
│   ├── 02_create_table_demonstracoes_contabeis.sql  # Criação da tabela contábil
│   ├── 03_insert_data_ans.sql                   # Popula tabela de operadoras
│   ├── 04_insert_data_contabeis.sql             # Popula tabela contábil
│   └── analytics_queries.sql                    # Consultas analíticas
├── exercise_4/
│   ├── backend/              # Backend estruturado (Flask)
│   │   ├── server.py            # Arquivo principal da API
│   ├── frontend/             # Frontend em Vue.js
│   │   ├── src/              # Código fonte Vue
│   └── postman/              # Coleção Postman
│       ├── API Operadoras.postman_collection.json  # Documentação das rotas
├── utils/                    # Funções utilitárias (ex: compressToZip)
├── data/                     # Arquivos CSV e PDFs processados
└── docker-compose.yml        # Configuração de containers
```

## 🔧 Tecnologias Utilizadas

### Backend (Python + Flask)

- Flask + Flask-CORS
- SQLAlchemy
- pdfplumber
- BeautifulSoup
- MySQL
- Docker

### Frontend (Vue.js)

- Vue 3
- Axios
- TypeScript
- HTML/CSS
- Docker

### Infra

- Docker e Docker Compose
- Variáveis de ambiente com dotenv

---

## 📦 Funcionalidades

### 🗂 Web Scraping

- Acessa o site da ANS e faz download automático dos anexos PDF
- Salva e comprime os arquivos localmente

### 📊 Processamento de Dados

- Extrai tabelas dos PDFs com `pdfplumber`
- Remove repetições de cabeçalhos
- Renomeia colunas para facilitar leitura
- Salva como CSV

### 🖥 API Flask

- Importa os dados para banco MySQL
- Disponibiliza endpoint `/search` com:
  - Filtro por nome fantasia, razão social ou CNPJ
  - Paginação
- Endpoint `/health` e `/test-db` para testes

### 🔍 Frontend (Vue.js)

- Interface de busca com campo dinâmico
- Visualização de operadoras em uma tabela
- Paginação de resultados

## 🐍 Ambiente Virtual Python (venv)

Para garantir que todas as dependências do projeto sejam instaladas de forma isolada, recomenda-se o uso de um ambiente virtual (`venv`).

### 📌 Verificando se o `venv` já está disponível

Execute o comando abaixo no terminal:

```bash
python3 -m venv --help
```

Se você não tiver o venv instalado, será necessário instalar o módulo. Em sistemas baseados em Debian/Ubuntu, você pode fazer isso com:

```bash
sudo apt install python3-venv
```

### ✅ Criando e ativando o ambiente virtual

1. Crie o ambiente virtual (recomendado rodar na raiz do projeto):

```bash
python3 -m venv venv
```

2. Ative o ambiente virtual:

- Linux / macOS:

```bash
source venv/bin/activate
```

- Windows (CMD):

```bash
venv\Scripts\activate
```

- Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

### Instalando as dependências

Com o ambiente virtual ativado, instale todas as dependências do projeto com(recomendado rodar na raiz do projeto):

```bash
pip install -r requirements.txt
```

### Rodando os scripts do projeto

### Pré-requisitos

- Exercício 1
  Acesse o diretório `exercise_1` e execute o seguinte comando:

```bash
cd exercise_1
python3 web_scraping.py
```

- Exercício 2
  Acesse o diretório `exercise_2` e execute o seguinte comando:

```bash
cd exercise_2
python3 data_transforming.py
```

- Exercício 3

Acesse o diretório exercise_3, em seguida abra o terminal no diretório para rodar os arquivos `.sql`, você deve primeiro acessar o MySQL pelo terminal. Use o seguinte comando:

```bash
mysql -u seu_usuario -p
```

Você será solicitado a digitar a senha do usuário. Após o login, selecione o banco de dados onde deseja executar o script:

```bash
USE nome_do_banco_de_dados;
```

Execute os scripts na seguinte ordem:

```bash
SOURCE 01_create_table_operadoras.sql;                 -- Criação da tabela de operadoras
SOURCE 02_create_table_demonstracoes_contabeis.sql;    -- Criação da tabela de demonstrações contábeis
SOURCE 03_insert_data_ans.sql;                         -- População da tabela de operadoras
SOURCE 04_insert_data_contabeis.sql;                   -- População da tabela de demonstrações contábeis
SOURCE analytics_queries.sql;                          -- Consulta das maiores despesas

```

## 🚀 Como Rodar a API e o Frontend

### Pré-requisitos

- Docker
- Docker Compose

### Passos

1. Crie um arquivo `.env` na raiz com as variáveis(Qualquer dúvida consulte o arquivo `.env.example`):

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=db
DB_NAME=ans_database
```

2. Execute no terminal o seguinte comando:

```bash
docker-compose up -d
```

Esse comando irá subir o container da aplicação, tanto o backend, quanto o frontend e o banco de dados.

<strong>
⚠️ Observação: Como o banco de dados é populado a partir de um arquivo CSV via API durante a inicialização, é necessário aguardar cerca de 2 minutos após a subida dos containers para que os dados estejam totalmente disponíveis nos endpoints.
</strong>

<br></br>

3.  Acesse a API:

```bash
    http://localhost:5000/
```

Consulte o arquivo API `Operadoras.postman_collection.json` no diretório `/exercise_4/postman` para mais informações sobre as rotas..

4. Acesse o Frontend:

```bash
    http://localhost:8080/
```

## Imagens do Projeto

![Buscar Operadoras](data/README_IMAGES/Screenshot%20from%202025-03-30%2013-33-51.png)
![Buscar Operadoras](data/README_IMAGES/Screenshot%20from%202025-03-30%2013-34-02.png)

## ✅ Considerações Finais

Este projeto demonstra a integração entre web scraping, manipulação de dados, API RESTful e interface web. Foi desenvolvido com foco em organização, clareza de código e separação de responsabilidades entre backend, frontend e infraestrutura.
