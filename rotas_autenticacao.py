from fastapi import APIRouter

roteador_autenticacao = APIRouter(
    prefix="/autenticacao", tags=["autenticacao"])


@roteador_autenticacao.get("/")
async def autenticacao():
    return {"mensagem": "voce entrou na rota de autenticacao"}
