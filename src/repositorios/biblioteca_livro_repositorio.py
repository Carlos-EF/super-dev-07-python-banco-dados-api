from src.banco_dados import conectar_biblioteca

from sqlalchemy.orm import Session

from src.database.models import Livro


def apagar(id: int) -> int:
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"

    dados = (id,)

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_apagadas = cursor.rowcount

    conexao.close()

    cursor.close()

    return linhas_apagadas


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


def obter_por_id(id: int):
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, quantidade_paginas, autor, preco, isbn, descricao FROM livros WHERE id= %s"

    dados = (id, )

    cursor.execute(sql, dados)

    registro = cursor.fetchone()

    if not registro:
        return None
    
    return {
        "id": registro[0],
        "titulo": registro[1],
        "quantidade_paginas": registro[2],
        "autor": registro[3],
        "preco": registro[4],
        "isbn": registro[5],
        "descricao": registro[6]
    }