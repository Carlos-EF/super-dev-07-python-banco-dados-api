from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

@app.get("/greetings")
def saudacoes():
    return {"mensagem": "Hello World"}


@app.get("/calculadora")
def calcular(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"resultado": soma}


# (query) vai depois da ? ex.: /calculadora/expert?operacao=somar&n1=100&n2=200
@app.get("/calculadora/expert")
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair", "dividir", "multiplicar"]:
        return HTTPException(
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
    

@app.get("/pessoa/nome-completo")
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
@app.get("/pessoa/calcular-ano-nascimento")
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
@app.get("/pessoa/imc")
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





# fastapi dev main.py
# 127.0.0.1/greetings