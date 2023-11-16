""" Ex.16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3m² e que a lata de tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tintas a
serem compradas e o proço total."""
import math
altura = float(input('Qual a Altura da parede? (m) '))
largura = float(input('Qual a Largura da parede? (m) '))
area = largura * altura
litro = area / 3
qtde_latas = math.ceil(litro / 18)
preco = qtde_latas * 80
print(f'{area} m² de área.')
print(f'Para esta área serão usados {litro:.2f} l de tinta, sendo necessário a compra de {qtde_latas:.2f} latas e '
      f'custará R$ {preco:.2f}.')
