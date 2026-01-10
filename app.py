from rotas_pedidos import roteador_pedidos
from rotas_autenticacao import roteador_autenticacao
from fastapi import FastAPI

app = FastAPI()

app.include_router(roteador_autenticacao)
app.include_router(roteador_pedidos)


@app.get("/")
def ola():
    return "ola mundo"