""" Ex.13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
"""
alt = float(input('Qual a sua altura? (m): '))
pesoH = (72.7 * alt) - 58
pesoM = (62.1 * alt) - 44.7

print(f'O peso ideal para um HOMEM com a altura informada é de {pesoH:.2f} kg.')
print(f'O peso ideal para um MULHER com a altura informada é de {pesoM:.2f} kg.')
