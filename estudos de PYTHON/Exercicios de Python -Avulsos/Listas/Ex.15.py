"""Ex.15 Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a) Mostre a quantidade de valores lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;
"""
notas = []
qtde_acima_media = 0
qtde_abaixo7 = 0
nota = 0
soma = 0  # Correção: Inicialização da soma deve ser 0, não 1

while nota != -1:
    nota = int(input('Digite uma nota: '))
    if nota != -1:
        notas.append(nota)
        soma += nota

# a) Mostre a quantidade de valores lidos;
qtde = len(notas)
print(f'Ao todo foram inseridos: {qtde} valores.')

# b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(f'Os valores inseridos foram: {notas}.')

# c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
notas.reverse()
print(f'Os valores inseridos na ordem INVERSA são: {notas}.')

# d) Calcule e mostre a soma dos valores;
print(f'A SOMA dos valores inseridos é: {soma}.')

# e) Calcule e mostre a média dos valores;
if qtde > 0:
    media = soma / qtde  # A média deve ser calculada apenas se houver pelo menos um valor inserido
    print(f'A MÉDIA dos valores inseridos é: {media}.')

# f) Calcule e mostre a quantidade de valores acima da média calculada;
for nota in notas:
    if nota > media:
        qtde_acima_media += 1
print(f'A quantidade de notas digitadas que foram ACIMA DA MÉDIA é: {qtde_acima_media}.')

# g) Calcule e mostre a quantidade de valores abaixo de sete;
for nota in notas:
    if nota < 7:
        qtde_abaixo7 += 1
print(f'A quantidade de notas digitadas ABAIXO de 7 é: {qtde_abaixo7}.')

# h) Encerre o programa com uma mensagem;
print('Programa Encerrado.')
