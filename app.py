from fastapi import FastAPI

app=FastAPI()

from rotas_autenticacao import roteador_autenticacao
from rotas_pedidos import roteador_pedidos

app.include_router(roteador_autenticacao)
app.include_router(roteador_pedidos)


@app.get("/")
def ola():
    return "ola mundo"

