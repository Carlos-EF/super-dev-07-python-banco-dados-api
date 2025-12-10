from pydantic import BaseModel


class AlunoCalcularMedia(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nome_completo: str


class AlunoFrequencia(BaseModel):
    nome: str
    quantidade_letivos: int
    quantidade_presenca: int


class ProdutoDesconto(BaseModel):
    nome: str
    preco_original: float
    percentual_desconto: float


class CarroAutonomia(BaseModel):
    modelo: str
    consumo_por_litro: float
    quantidade_combustivel: float


class PedidoTotal(BaseModel):
    descricao: str
    quantidade: int
    valor_unitario: float