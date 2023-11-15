""" Ex.16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
    O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas
    seguintes situações:
    - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
    fazer pedir os demais valores, sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math
from math import sqrt
from fractions import Fraction

print(f'\nVamos Resolver uma equação de segundo grau?')
a = int(input('Digite o valor "a" da equação: '))
while True:

    if a == 0:
        print('Esta não será uma equação de segundo grau.')
        break

    b = int(input('Digite o valor "b" da equação: '))
    c = int(input('Digite o valor "c" da equação: '))

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print(f'\nPara os valores informados, o delta é negativo: ({delta}), por isso não existe Raízes Reais.')
        break
    elif delta == 0:
        x = (-b) / (2 * a)
        print(f'\nPara os valores informados, o delta é ZERO: ({delta}), por isso as raízes da equação são iguais e '
              f'se valor é: {x} ')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'\nPara os valores informados, o delta é: ({delta}), por isso possui DUAS raízes Reais e diferentes'
              f'que são {x1} e {x2}.')
    break
print(f'\nPrograma Encerrado!')
