""" Ex.48 Faça um programa que peça um número inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""
num = int(input('Digite um número: '))
num_string = str(num)
invertido = num_string[::-1]

print("Número original:", num)
print("Número invertido:", invertido)
