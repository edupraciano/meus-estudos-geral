# Ex.06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Qual o tamanho do raio? '))
import math
area = math.pi * raio ** 2
print(f'Para {raio} cm de raio, temos {area:.2f} cm² de área.')
