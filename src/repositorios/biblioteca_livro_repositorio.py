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


def editar(id: int, titulo: str, quantidade_paginas: int, autor: str, preco: float, isbn: str, descricao: str) -> int:
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo= %s, quantidade_paginas= %s, autor= %s, preco= %s, isbn= %s, descricao= %s WHERE id = %s"

    dados = (titulo, quantidade_paginas, autor, preco, isbn, descricao, id)

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_alteradas = cursor.rowcount

    cursor.close()

    conexao.close()

    return linhas_alteradas


def obter_todos(db: Session):
    livros = db.query(Livro).all()

    return livros


def obter_por_id(db: Session, id: int):
    livro = db.query(Livro).filter(Livro.id == id).first()

    return livro
