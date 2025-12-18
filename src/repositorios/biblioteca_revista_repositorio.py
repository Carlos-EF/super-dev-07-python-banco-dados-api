from datetime import date
from sqlalchemy.orm import Session

from src.database.models import Revista


def obter_todos(db: Session):
    revistas = db.query(Revista).all()

    return revistas


def obter_por_id(db: Session, id: int):
    revista = db.query(Revista).filter(Revista.id == id).first()

    return revista


def cadastrar(db: Session, titulo: str, edicao: int, data_publicacao: date, editora: str):
    revista = Revista(
        titulo= titulo,
        edicao= edicao,
        data_publicacao= data_publicacao,
        editora= editora,
    )

    db.add(revista)
    db.commit()
    db.refresh(revista)

    return revista


def apagar(db: Session, id: int) -> int:
    revista = db.query(Revista).filter(Revista.id == id).first
    if not revista:
        return 0
    
    db.delete(revista)
    db.commit()
    return 1


def editar(db: Session, id: int,titulo: str, edicao: int, data_publicacao: date, editora: str) -> int:
    revista = db.query(Revista).filter(Revista.id == id).first()
    if not revista:
        return 0
    
    revista.titulo = titulo
    revista.edicao = edicao
    revista.data_publicacao = data_publicacao
    revista.editora = editora

    db.commit()
    return 1