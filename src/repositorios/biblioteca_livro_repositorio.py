from src.banco_dados import conectar_biblioteca

from sqlalchemy.orm import Session

from src.database.models import Livro


def apagar(db: Session, id: int) -> int:
    livro = db.query(Livro).filter(Livro.id == id).first()
    if not livro:
        return 0
    
    db.delete(livro)
    db.commit()
    return 1


def cadastrar(db: Session, titulo: str, quantidade_paginas: int, autor: str, preco: float, isbn: str, descricao: str):
    livro = Livro(
        titulo=titulo,
        quantidade_paginas=quantidade_paginas,
        autor=autor,
        preco=preco,
        isbn=isbn,
        descricao=descricao
    )

    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro


def editar(db: Session, id: int, titulo: str, quantidade_paginas: int, autor: str, preco: float, isbn: str, descricao: str) -> int:
    livro = db.query(Livro).filter(Livro.id == id).first()
    if not livro:
        return 0
    
    livro.titulo = titulo
    livro.quantidade_paginas = quantidade_paginas
    livro.autor = autor
    livro.preco = preco
    livro.isbn = isbn
    livro.descricao = descricao
    db.commit()
    return 1
    


def obter_todos(db: Session):
    livros = db.query(Livro).all()

    return livros


def obter_por_id(db: Session, id: int):
    livro = db.query(Livro).filter(Livro.id == id).first()

    return livro
