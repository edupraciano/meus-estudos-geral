"""
Ex. 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um 
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

data_atual = date.today()
ano_atual = data_atual.year
cont = 1
sair = ""
dados = {}
while True:
    nome = str(input(f"Digite o nome do {cont}º trabalhador: "))

    while True:
        try:
            ano_de_nascimento = int(input(f"Digite o ano de nascimento de {nome}: "))
            break
        except ValueError:
            print("Isso não é um ano válido. Por favor, tente novamente.")

    while True:
        try:
            ctps = int(input("Digite o número da Carteira de Trabalho: "))
            break
        except ValueError:
            print("Isso não é um número válido. Por favor, tente novamente.")

    idade = ano_atual - ano_de_nascimento

    if ctps == 0:
        dados[nome] = {"idade": idade, "CTPS": "Não Possui CTPS"}
    else:
        while True:
            try:
                ano_de_contratacao = int(input("Qual foi o ano da Contratação? "))
                break
            except ValueError:
                print("Isso não é um ano válido. Por favor, tente novamente.")

        while True:
            try:
                salario = float(input("Qual o Salário do Trabalhador? "))
                break
            except ValueError:
                print("Isso não é um valor válido. Por favor, tente novamente.")

        anos_trabalhados = ano_atual - ano_de_contratacao
        anos_para_aposentar = 30 - anos_trabalhados
        idade_quando_aposentado = idade + anos_para_aposentar

        dados[nome] = {
            "idade": idade,
            "ctps": ctps,
            "Ano da contratacao": ano_de_contratacao,
            "Salário": salario,
            "Anos para aposentar": anos_para_aposentar,
            "Idade quando Aposentado": idade_quando_aposentado,
        }

    sair = ""
    while sair not in ["S", "N"]:
        sair = str(input("Deseja SAIR? [S/N] ")).strip().upper()[0]

    print("-=" * 30)
    if sair == "S":
        break
    cont += 1

print(f'\n{"== Estes são os Trabalhadores Cadastrados ==":^50}\n')
for k, v in dados.items():
    print(f"Os Dados de {k} são:")
    print(f"idade: {v['idade']}")
    print(f"ctps: {v['CTPS']}")
    if "Ano da contratacao" in v:
        print(f"Ano da contratacao: {v['Ano da contratacao']}")
    if "Salário" in v:
        print(f"Salário: R$ {v['Salário']:.2f}")
    if "Anos para aposentar" in v:
        print(f"Anos para aposentar: {v['Anos para aposentar']}")
    if "Idade quando Aposentado" in v:
        print(f'{k} terá {v["Idade quando Aposentado"]} ao se aposentar.')
    print("-" * 30)
print("\nPrograma Encerrado!")
