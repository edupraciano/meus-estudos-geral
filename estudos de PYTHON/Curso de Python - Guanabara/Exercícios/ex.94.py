"""
Ex. 94 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
cont = soma = 0
mulheres = []
acima_da_media = []
pessoa = {}
listaGeral = []
while True:
    lista_das_idade = []
    pessoa["Nome"] = (
        str(input(f"Digite o nome da {cont + 1}ª pessoa: ")).strip().upper()
    )
    pessoa["Idade"] = int(input(f"Digite a idade da {cont + 1}ª pessoa: "))
    pessoa["Sexo"] = ""
    while True:
        pessoa["Sexo"] = (
            str(input(f"Digite o Sexo da {cont + 1}ª pessoa: [M/F] "))
            .strip()
            .upper()[0]
        )
        if pessoa["Sexo"] in ["M", "F"]:
            break
        else:
            print("[ERRO] Por favor Escolha entre M ou F")

    if pessoa["Sexo"] == "F":
        mulheres.append(pessoa["Nome"][:])

    listaGeral.append(pessoa)
    cont += 1
    soma += pessoa["Idade"]
    lista_das_idade.append(pessoa["Idade"])
    soma_das_idades = sum(lista_das_idade)

    media = soma / cont

    if pessoa["Idade"] > media:
        acima_da_media.append(pessoa["Nome"])

    sair = ""
    while True:
        sair = str(input("Deseja SAIR? [S/N] ")).strip().upper()[0]
        if sair in ["S", "N"]:
            break
        print("[ERRO] Digite S para sair ou N para continuar")

    if sair == "S":
        break

print("-=" * 30)
# A) Quantas pessoas foram cadastradas
print(f"Ao todo foram cadastradas {len(listaGeral)} pessoas.")

# B) A média de idade
print(f"A média das idades é de : {media:.1f} anos")

# C) Uma lista com as mulheres
print(f"A lista de múlheres é : {mulheres}")

# D) Uma lista de pessoas com idade acima da média
print(f"As pessoas com idade acima da média são: {acima_da_media}")
print(f"A lista Geral com todas os dicionários das pessoas é: {listaGeral}")
