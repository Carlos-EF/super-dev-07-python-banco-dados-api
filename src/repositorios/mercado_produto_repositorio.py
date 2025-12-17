from src.banco_dados import conectar

from sqlalchemy.orm import Session, contains_eager

from src.database.models import Produto

def cadastrar(db: Session, nome: str, id_categoria: int):
    produto = Produto(nome=nome, id_categoria=id_categoria)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


def editar(db: Session, id: int, nome: str, id_categoria: int):
    # SELECT * FROM produtos WHERE id = ?
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return 0
    
    produto.nome = nome
    produto.id_categoria = id_categoria
    # UPDATE produtos SET nome = ?, id_categoria = ? WHERE id = ?
    db.commit()
    return 1


def apagar(db: Session, id: int):
    # SELECT * FROM produtos WHERE id = ?
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return 0

    db.delete(produto)
    # DELETE FROM produtos WHERE id = ?
    db.commit()
    return 1 


def obter_todos(db: Session):
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = """select
	# produtos.id,
	# produtos.nome,
	# categorias.id,
	# categorias.nome
	# from produtos
	# inner join categorias on (produtos.id_categoria = categorias.id)"""
    # cursor.execute(sql)
    # registros = cursor.fetchall()
    # produtos = []
    # for registro in registros:
    #     produto = {
    #         "id": registro[0],
    #         "nome": registro[1],
    #         "categoria": {
    #             "id": registro[2],
    #             "nome": registro[3]
    #         }
    #     }
    #     produtos.append(produto)
    # return produtos

    produtos = db.query(Produto).options(contains_eager(Produto.categoria)).all()

    return produtos


def obter_por_id(db:Session, id: int):
    produto = db.query(Produto)\
        .options(contains_eager(Produto.categoria))\
        .filter(Produto.id == id)\
        .first()

    return produto
