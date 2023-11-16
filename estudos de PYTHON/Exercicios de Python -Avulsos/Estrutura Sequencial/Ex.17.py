""" Ex.17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações: - comprar apenas latas de 18 litros; -
comprar apenas galões de 3,6 litros; - misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math
area = float(input('Qual a área da parede? (m²) '))
litro = area / 6

# Adiciona 10% de folga
litro += litro * 0.1

# para Latas
qtde_latas = math.floor(litro / 18)
preco_latas = qtde_latas * 80

# Para galões
litro_restante = litro - (qtde_latas * 18)
qtde_galoes = math.ceil(litro_restante / 3.6)
preco_galoes = qtde_galoes * 25

preco_total = preco_latas + preco_galoes

print()
print(f'{area} m² de área.')
print()
print('-=' * 50)
print('Se você optar por comprar apenas Latas de tinta de 18l, estas são as informações necessárias...')
print(f'Para esta área serão usados {litro:.2f} l de tinta, sendo necessário a compra de {qtde_latas} latas e '
      f'custará R$ {preco_latas:.2f}.')
print('-=' * 50)
print('Se você optar por comprar apenas Galoes de tinta de 3.6l, estas são as informações necessárias...')
print(f'Para esta área serão usados {litro:.2f} l de tinta, sendo necessário a compra de {qtde_galoes} galoes e '
      f'custará R$ {preco_galoes:.2f}.')
print('-=' * 50)
print('Se você optar por misturar Latas e Galões de tinta, estas são as informações necessárias...')
print(f'Para esta área serão usados {litro:.2f} l de tinta, sendo necessário a compra de {qtde_latas} latas e {qtde_galoes} galões e '
      f'custará R$ {preco_total:.2f}.')
print('-=' * 50)
