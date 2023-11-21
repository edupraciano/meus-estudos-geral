""" Ex.35 Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário."""
num = int(input('Digite um número: '))
num_primos = []
for i in range(1, num + 1):
    divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1
        if divisores > 2:
            break
    if divisores == 2:
        num_primos.append(i)

print(f'A lista dos números primos é {num_primos}')
