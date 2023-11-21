# Ex.04 Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.
lista_consoantes = []
cont = 0
for i in range(10):
    caracter = input(f'Entre com o {i + 1}º caracter: ')[0]
    if caracter not in ['a', 'e', 'i', 'o', 'u']:
        lista_consoantes.append(caracter)
        cont += 1

print(f'Foram encontrados {cont} caracteres na lista de consoantes, são eles: {lista_consoantes}')
