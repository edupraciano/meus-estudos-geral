""" Ex.10 Faça um programa que receba dois números inteiros e gere os números inteiros no intervalo compreendido por
eles."""
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

for c in range(num1, num2 + 1):
    print(f' > {c}', end='')