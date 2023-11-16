# Ex.10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input('DIgite a temperatura em º Celsius: '))
F = (C * 9 / 5) + 32
print(f'{C}ºC correspondem a {F:.2f}ºF')
