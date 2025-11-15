# API de Gerenciamento de Pedidos — Willy

Este projeto é uma réplica estudada e testada da API fornecida pelo professor Claudio Ulisses.  
Ele implementa um CRUD completo de pedidos usando:

- FastAPI  
- SQLAlchemy  
- Pydantic  
- Swagger UI  
- Uvicorn  

---

# Tecnologias Usadas

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.30-red?logo=python)](https://docs.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.29.0-purple?logo=python)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.7.1-blue?logo=python)](https://docs.pydantic.dev/)

---

# Estrutura do Projeto

IWS/
└── rest/
├── app.py
├── config/
├── models/
├── repositories/
├── services/
├── controllers/
└── schemas/


---

# Como Executar o Projeto

# 1. Instale as dependências


```bash
pip install -r requirements.txt

ou 

pip install fastapi uvicorn sqlalchemy pydantic


# 2. Rode o servidor

python app.py

# 3️. Acesse o Swagger UI

🔗 http://localhost:8000/docs

🔗 http://localhost:8000/redoc


# Observações

API testada e validada com sucesso.

Rotas funcionando em ambiente local.

Código replicado do exemplo proposto pelo professor para estudo.

# Repositório do Projeto

https://github.com/WillyFortunasc/MeusProjetos_Python/tree/main/Rest_willy.pedidos

## Tela do Swagger UI


