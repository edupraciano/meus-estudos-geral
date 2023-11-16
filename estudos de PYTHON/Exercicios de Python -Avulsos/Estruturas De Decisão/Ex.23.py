""" Ex.23 Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
    Dica: utilize uma função de arredondamento.
"""
entrada = input('Digite um valor: ')
numero = float(entrada)
if numero == int(numero):
    print(f'\nEste número é Inteiro.')
else:
    print(f'\nEste número é Decimal.')

# uma OUTRA Maneira de Resolver
'''entrada = input('Digite um valor: ')
if '.' in entrada:
    print(f'\nEste número é Decimal.')
else:
    print(f'\nEste número é Inteiro.')
'''


