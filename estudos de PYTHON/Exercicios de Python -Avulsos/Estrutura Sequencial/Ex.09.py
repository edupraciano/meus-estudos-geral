""" Ex.09 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus
Celsius. C = 5 * ((F-32) / 9).
"""
F = float(input('DIgite a temperatura em ºFahrenheit: '))
C = 5 * ((F-32) / 9)
print(f'{F}ºF correspondem a {C:.2f}ºC')

