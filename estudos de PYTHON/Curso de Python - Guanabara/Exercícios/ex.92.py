"""
Ex. 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dados = {}
dados["Nome"] = str(input("Digite o nome do trabalhador: "))
dados["Nascimento"] = int(input("Digite o ano de Nascimento: "))
dados["ctps"] = int(input("Digite o número da CTPS: [ 0 se Não tiver ] "))
if dados["ctps"] == 0:
    print("-=" * 25)
    print("Dados do Trabalhador")
    for k, v in dados.items():
        print(f"{k} ==> {v}")
        print("-=" * 25)
        break
else:
    ano_atual = datetime.now().year
    dados["Idade"] = ano_atual - dados["Nascimento"]
    dados["Contratação"] = int(input("Qual o ano da contratação? "))
    dados["Salário"] = int(input("Digite o Salário R$ "))
    anos_trabalhados = ano_atual - dados["Contratação"]
    anos_para_aposentar = 30 - anos_trabalhados
    dados["Idade ao se aposentar"] = dados["Idade"] + anos_para_aposentar
    print()
    print("-=" * 20)
    print("Dados do Trabalhador")
    for k, v in dados.items():
        print(f"{k} ==> {v}")
    print("-=" * 20)
