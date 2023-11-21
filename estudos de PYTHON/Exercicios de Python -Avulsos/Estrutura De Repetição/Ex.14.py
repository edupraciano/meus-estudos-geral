""" Ex.14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
quantidade de números impares."""
pares = impares = 0
for n in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Ao todo foram impressos {pares} números pares')
print(f'Ao todo foram impressos {impares} números impares')
