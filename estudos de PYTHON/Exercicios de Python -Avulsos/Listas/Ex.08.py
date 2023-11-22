"""Ex.08 Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
lista_idade = []
lista_altura = []
for i in range(5):

    idade = int(input(f'Entre com a idade da {i + 1}ª pessoa: '))
    altura = float(input(f'Entre com a altura da {i + 1}ª pessoa: '))

    lista_idade.append(idade)
    lista_altura.append(altura)

print(f'A lista de idade com a ordem de entrada é: {lista_idade}')
print(f'A lista de altura com a ordem de entrada é: {lista_altura}')

lista_idade.reverse()
lista_altura.reverse()

print(f'A lista de idade com a ordem invertida é: {lista_idade}')
print(f'A lista de altura com a ordem invertida é: {lista_altura}')
