from fastapi import FastAPI, HTTPException
from datetime import datetime

from classes import AlunoCalcularMedia, AlunoFrequencia, CarroAutonomia, CategoriaCriar, CategoriaEditar, LivroCriar, PedidoTotal, ProdutoCriar, ProdutoDesconto, ProdutoEditar
from src.repositorios import biblioteca_livro_repositorio, mercado_categoria_repositorio, mercado_produto_repositorio

app = FastAPI()

@app.get("/greetings", tags=["Saudações"])
def saudacoes():
    return {"mensagem": "Hello World"}


@app.get("/calculadora", tags=["Calculadora"])
def calcular(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}


# (query) vai depois da ? ex.: /calculadora/expert?operacao=somar&n1=100&n2=200
@app.get("/calculadora/expert", tags=["Calculadora"])
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair", "dividir", "multiplicar"]:
        raise HTTPException(
            status_code=400,
            detail="Operação inválida. Opcões disponíveis [somar, subtrair, dividir, multiplicar]"
        )
    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "dividir":
        resultado = n1 / n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "multiplicar":
        resultado = n1 * n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    

@app.get("/pessoa/nome-completo", tags=["Pessoas"])
def concatenar_nome(nome: str, sobrenome: str):
    nome_completo =  nome + " " + sobrenome
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "nomeCompleto": nome_completo
    }


# Criar um endpoint 'pessoa/calcular-ano-nascimento' para calcular o ano de nascimento
#   Query param: idade
#   Calcular o ano de nascimento
#   Retornar {"anoNascimento": 1991}


@app.get("/pessoa/calcular-ano-nascimento", tags=["Pessoas"])
def calcular_ano_nascimento(idade: int):
    data_atual = datetime.now()

    ano_atual = data_atual.year

    ano_nascimento = ano_atual - idade
    return {
        "idade": idade,
        "anoNascimento": ano_nascimento
    }


# Criar um endpoint 'pessoa/imc' para calcular o imc da pessoa
#   Query param: altura, peso
#   Calcular o imc
#   Retornar {"imc": 20.29}
# Alterar o endpoint 'pessoa/imc' para retornar o status do imc
#   Descobrir o status do IMC
#   Retornar {"imc"': 20.29, "Obesidade III"}


@app.get("/pessoa/imc", tags=["Pessoas"])
def calcular_imc(altura: float, peso: float):
    imc = peso / (altura * altura)
    if imc < 18.5:
        status = "Magreza"
    elif imc >= 18.5 and imc <= 24.9:
        status = "Normal"
    elif imc >= 25.0 and imc <= 29.9:
        status = "Sobrepeso"
    elif imc >= 30.0 and imc <= 39.9:
        status = "Obesidade"
    elif imc >= 40.0:
        status = "Obesidade Grave"

    return {
        "imc": f"""{imc:.2f}""",
        "status": status
    }


@app.post("/aluno/calcular-media", tags=["Alunos"])
def calcular_media(alunos_dados: AlunoCalcularMedia):
    nota1 = alunos_dados.nota1

    nota2 = alunos_dados.nota2

    nota3 = alunos_dados.nota3

    media = (nota1 + nota2 + nota3) / 3

    return {
        "media": media,
        "nome_completo": alunos_dados.nome_completo
    }


# Ex.1 Criar um endpoint do tipo POST /aluno/calcular-frequencia
# Criar uma classe AlunoFrequencia
#   nome
#   quantidade_letivos
#   quantidade_presencas
# Payload:
#   nome do aluno
#   quantidade letivos
#   quantidade presencas
#   
#   qtd letivos     100
#   qtd presencas   
#   (qtd presencas * 100) / qtd letivos
@app.post("/aluno/calcular-frequencia", tags=["Alunos"])
def calcular_frequencia(aluno_dados: AlunoFrequencia):
    presenca = aluno_dados.quantidade_presenca

    letivos = aluno_dados.quantidade_letivos

    frequencia = (presenca * 100) / letivos


    return {
        "nome do aluno": aluno_dados.nome,
        "quantidade letivos": aluno_dados.quantidade_letivos,
        "quantidade presenca": aluno_dados.quantidade_presenca,
        "frequncia": frequencia
    }


# Ex.2 Criar um endpoint do tipo POST /produto/calcular-desconto
# Criar uma classe ProdutoDesconto
#   nome
#   preco_original
#   percentual_desconto
# Payload:
#   nome do produto
#   preço original
#   percentual de desconto (0 a 100)
# Fórmulas:
#   valor_desconto = (preco_original * percentual_desconto) / 100
#   preco_final = preco_original - valor_desconto
@app.post("/produto/calcular-desconto", tags=["Atividades"])
def calcular_desconto(produto_dados: ProdutoDesconto):
    preco_original = produto_dados.preco_original

    percentual_desconto = produto_dados.percentual_desconto

    valor_desconto = (preco_original * percentual_desconto) / 100
    
    preco_final = preco_original - valor_desconto

    return {
        "nome do produto": produto_dados.nome,
        "preco original": preco_original,
        "percentual de desconto(0 a 100)": percentual_desconto,
        "valor do desconto": valor_desconto,
        "preco final": preco_final
    }


# Ex.3 Criar um endpoint do tipo POST /carro/calcular-autonomia
# Criar uma classe CarroAutonomia
#   modelo
#   consumo_por_litro
#   quantidade_combustivel
# Payload:
#   modelo do carro
#   consumo por litro (km/l)
#   quantidade de combustível no tanque (litros)
#
# Fórmula:
#   autonomia = consumo_por_litro * quantidade_combustivel
@app.post("/carro/calcular-autonomia", tags=["Atividades"])
def calcular_autonomia(carro_dados: CarroAutonomia):
    consumo_litro = carro_dados.consumo_por_litro

    quantidade_combustivel = carro_dados.quantidade_combustivel

    autonomia = consumo_litro * quantidade_combustivel

    return {
        "modelo": carro_dados.modelo,
        "consumo por litro(KM/l)": consumo_litro,
        "quantidade de combustivel no tanque (litros)": quantidade_combustivel,
        "autonomia do carro": autonomia
    }


# Ex.4 Criar um endpoint do tipo POST /pedido/calcular-total
# Criar uma classe PedidoTotal
#   descricao
#   quantidade
#   valor_unitario
# Payload:
#   descrição do pedido
#   quantidade de itens
#   valor unitário
#
# Fórmulas:
#   subtotal = quantidade * valor_unitario
#   taxa = subtotal * 0.05  (5% de taxa de serviço)
#   total = subtotal + taxa


@app.post("/pedido/calcular-total", tags=["Atividades"])
def calcular_pedido(pedido_dados: PedidoTotal):
    quantidade = pedido_dados.quantidade

    valor_unitario = pedido_dados.valor_unitario

    subtotal = quantidade * valor_unitario

    taxa = subtotal * 0.05

    total = subtotal +  taxa

    return {
        "descrição do pedido": pedido_dados.descricao,
        "quantidade de itens": quantidade,
        "valor unitário": valor_unitario,
        "subtotal": subtotal,
        "taxa adicional": taxa,
        "total final": total
    }


@app.get("/api/v1/categorias", tags=["Categorias"])
def listar_categorias():
    categorias = mercado_categoria_repositorio.obter_todos()
    return categorias


@app.post("/api/v1/categorias", tags=["Categorias"])
def cadastrar_categoria(categoria: CategoriaCriar):
    mercado_categoria_repositorio.cadastrar(categoria.nome)
    return {
        "status": "OK"
    }


@app.delete("/api/v1/categorias/{id}", tags=["Categorias"])
def apagar_categoria(id: int):
    linhas_afetadas = mercado_categoria_repositorio.apagar(id)

    if linhas_afetadas == 1:
        return {
            "status": "OK"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    

@app.put("/api/v1/categorias/{id}", tags=["Categorias"])
def alterar_categoria(id: int, categoria: CategoriaEditar):
    linhas_afetadas = mercado_categoria_repositorio.editar(id, categoria.nome)
    if linhas_afetadas == 1:
        return {
            "status": "OK"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    

@app.get("/api/v1/categorias/{id}", tags=["Categorias"])
def buscar_categoria_por_id(id: int):
    categoria = mercado_categoria_repositorio.obter_por_id(id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    return categoria


# ---------------------------------------------------------- Produtos -----------------------------------------------------------------------------------------------


@app.get("/api/v1/produtos", tags=["Produtos"])
def listar_todos_produtos():
    produtos = mercado_produto_repositorio.obter_todos()
    return produtos


@app.post("/api/v1/produtos", tags=["Produtos"])
def cadastrar_produto(produto: ProdutoCriar):
    mercado_produto_repositorio.cadastrar(produto.nome, produto.id_categoria)
    return {
        "status": "OK"
    }


@app.put("/api/v1/produtos/{id}", tags=["Produtos"])
def alterar_produto(id: int, produto: ProdutoEditar):
    linhas_afetadas = mercado_produto_repositorio.editar(id, produto.nome, produto.id_categoria)

    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return {
        "status": "OK"
    }


@app.delete("/api/v1/produtos/{id}", tags=["Produtos"])
def apagar_produto(id: int):
    linhas_afetadas = mercado_produto_repositorio.apagar(id)

    if linhas_afetadas != 1:
        raise HTTPException(status_code= 404, detail="Produto não encontrado")
    
    return {
        "status": "OK"
    }


@app.get("/api/v1/produtos/{id}", tags=["Produtos"])
def obter_produto_por_id(id: int):
    produto = mercado_produto_repositorio.obter_por_id(id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto


# ---------------------------------------------------------- Livros -----------------------------------------------------------------------------------------------


@app.get("/api/v1/livros", tags=["Livros"])
def listar_livros():
    livros = biblioteca_livro_repositorio.obter_todos()
    return livros


@app.get("/api/v1/livros/{id}", tags=["Livros"])
def obter_livro_por_id(id: int):
    livro = biblioteca_livro_repositorio.obter_por_id(id)

    if livro is None:
        raise HTTPException(status_code= 404, detail="Livro não encontrado")
    
    return livro


@app.post("/api/v1/livros", tags=["Livros"])
def cadastrar_livro(livro: LivroCriar):
    biblioteca_livro_repositorio.cadastrar(livro.titulo, livro.quantidade_paginas, livro.autor, livro.preco, livro.isbn, livro.descricao)

    return {
        "status": "OK"
    }


# fastapi dev main.pys/
# 127.0.0.1/greetings///