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

![1. Swagger aberto](images/1_1.png)
![1.1 Swagger aberto](/1_2.png)
![2. Redoc aberto](images/2.png)
![3.1 get pedidos](images/3_1.png)
![3.2 get pedidos](images/3_2.png)
![4.1 post pedidos](images/4_1.png)
![4.2 post pedidos](images/4_2.png)
![5.1 get pedidos_pedidos id](images/5_1.png)
![5.2 get pedidos_pedidos id](images/5_2.png)
![6.1 Put Pedidos_pedidos id](images/6_1.png)
![6.2 Put Pedidos_pedidos id](images/6_2.png)
![7.1 Delete pedidos_pedidos id](images/7_1.png)
![7.2 Delete pedidos_pedidos id](images/7_2.png)
![8 Get Clientes_listar clientes](images/8.png)
![9.1 Post Clientes_listar clientes](images/9_1.png)
![9.2 Post Clientes_listar clientes](images/9_2.png)
![10.1 Get Clientes_clientes id](images/10_1.png)
![10.2 Get Clientes_clientes id](images/10_2.png)
![11.1 Put Clientes_clientes id](images/11_1.png)
![11.2 Put Clientes_clientes id](images/11_2.png)
![12.1 Delete Clientes_clientes id](images/12_1.png)
![12.2 Delete Clientes_clientes id](images/12_2.png)