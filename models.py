from sqlalchemy import create_engine, column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
# crio a cpnexao com o db
db = create_engine("sqlite:///banco.db")
# crio a base do db
base = declarative_base()
# crio as classes/tabelas do db


class Usuario(base):
    __tablename__ = "usuarios"

    id = column("id", Integer, primarykey=True, autoincrement=True)
    nome = column("nome", String)
    email = column("email", String, nullable=False)
    semha = column("senha", String)
    ativo = column("ativo", Boolean)
    admin = column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedidos(base):
    __tablename__ = "pedidos"

    id = column("id", Integer, primarykey=True, autoincrement=True)
    status = column("status", String)
    Usuario = column("usuario", ForeignKey("usuarios.id"))
    preco = column("preco", float)
    # itens
# executo a criaçao dos metadados do db (crio efetivamente o banco)
