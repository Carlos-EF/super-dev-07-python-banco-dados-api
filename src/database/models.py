from sqlalchemy import Column, Date, Double, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

# Temos uma classe chamada Categoria que herda as propriedades e métodos da Base
class Categoria(Base):
    __tablename__ = "categorias"

    # Coluna da PK id do tipo inteiro auto incrementável
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Coluna do nome que n permite nulo
    nome = Column(String(255), nullable=False)

    produto = relationship("Produto", back_populates="categoria")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(14), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    limite = Column(Double, nullable=True)

    # nullable=False campo é obrigatório
    # nullable=True campo não é obrigatório


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    # FK que relaciona a PK (categorias.id)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="produto")


# -------------------------------------------------------------------- Biblioteca : Livro -----------------------------------------------------------------------

class Livro(Base):
    __tablename__= "livros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    quantidade_paginas = Column(Integer, nullable=False)
    autor = Column(String(100), nullable=False)
    preco = Column(Double, nullable=False)
    isbn = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)

# -------------------------------------------------------------------- Biblioteca : Mangá -----------------------------------------------------------------------

class Manga(Base):
    __tablename__ = "manga"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    volume = Column(Integer, nullable=False)
    autor = Column(String(100), nullable=False)
    data_lancamento = Column(Date, nullable=False)


# -------------------------------------------------------------------- Biblioteca : Revista -----------------------------------------------------------------------

class Revista(Base):
    __tablename__ = "revista"

    id = Column(Integer, primary_key= True, autoincrement=True)
    titulo = Column(String(100), nullable=False)