from datetime import date
from sqlalchemy.orm import Session

from src.database.models import Cliente


def cadastrar(db: Session, nome: str, cpf: str, data_nascimento: date, limite: float):
    cliente = Cliente(
        nome=nome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        limite=limite
    )

    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente