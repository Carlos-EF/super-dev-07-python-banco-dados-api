from src.banco_dados import conectar_biblioteca
from datetime import date
from sqlalchemy.orm import Session

from src.database.models import Manga

def apagar(db: Session, id: int) -> int:
    livro = db.query(Manga).filter(Manga.id == id).first()
    if not livro:
        return 0
    
    db.delete(livro)
    return 1


def cadastrar(db: Session, nome: str, volume: int, autor: str, data_lancamento: date):
    manga = Manga(
        nome= nome,
        volume= volume,
        autor= autor,
        data_lancamento= data_lancamento,
    )
    db.add(manga)
    db.commit()
    db.refresh(manga)
    return manga


def editar(db: Session, id: int, nome: str, volume: int, autor: str, data_lancamento: date) -> int:
    manga = db.query(Manga).filter(Manga.id == id).first()
    if not manga:
        return 0

    manga.nome = nome
    manga.volume = volume
    manga.autor = autor
    manga.data_lancamento = data_lancamento
    db.commit()
    return 1
    

def obter_todos(db: Session):
    mangas = db.query(Manga).all()

    return mangas


def obter_por_id(db: Session, id: int):
    manga = db.query(Manga).filter(Manga.id == id).first()

    return manga

