# Ex.18 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos
# valores.
N = int(input('Digite a quantidade de números que vc deseja inserir: '))

num = int(input('Digite o 1º número: '))
menor = maior = soma = num
for c in range(2, N + 1):
    num = int(input(f'Digite o {c}º número: '))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")
print(f"A soma dos valores é {soma}")
