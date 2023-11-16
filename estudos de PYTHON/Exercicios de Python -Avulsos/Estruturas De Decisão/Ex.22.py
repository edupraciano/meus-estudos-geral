""" Ex.22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
    Dica: utilize o operador módulo (resto da divisão).
"""
num = int(input('Digite um número inteiro positivo: '))
if num % 2 ==0:
    print(f'\nO número {num} é PAR.')
else:
    print(f'\nO número {num} é IMPAR.')