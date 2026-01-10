from fastapi import APIRouter

roteador_pedidos=APIRouter(prefix="/pedidos",tags=["pedidos"])

@roteador_pedidos.get("/")
async def pedidos():
    return {"mensagem":"voce acessou a rota de pedidos"}