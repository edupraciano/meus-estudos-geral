""" Ex.15 Faça um programa que leia os três lados de um triângulo.
    O programa deverá informa se os 3 lados podem forma um triângulo e o seu tipo (Equilátero, Isosceles, ou Escaleno)
"""
l1 = float(input('Valor do 1º lado: '))
l2 = float(input('Valor do 2º lado: '))
l3 = float(input('Valor do 3º lado: '))
tipo = ''

if l1 == l2 and l1 == l3 and l2 == l3:
    tipo = 'Equilátero, pois possui os 3 lados iguais.'
elif l1 != l2 and l2 != l3 and l1 != l3:
    tipo = 'Escaleno, pois possui os 3 lados diferentes.'
elif l1 == l2 or l1 == l3 or l2 == l3:
    tipo = 'Isosceles, pois possui os 2 lados iguais.'

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    print(f'Estes lados formam um Triângulo e seu tipo é: {tipo}')
else:
    print('Estes lados NÃO formam um Triângulo')
