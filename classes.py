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


class CategoriaCriar(BaseModel):
    nome: str


class CategoriaEditar(BaseModel):
    nome: str


class ProdutoCriar(BaseModel):
    nome: str
    id_categoria: int


class ProdutoEditar(BaseModel):
    nome: str
    id_categoria: int