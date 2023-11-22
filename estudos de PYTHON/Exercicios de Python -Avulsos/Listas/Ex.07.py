# Ex.07 Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
for i in range(5):
    num = int(input(f'DIgite o {i + 1}º número: '))
    lista.append(num)

print(f'Os números digitados são: {lista}')
soma = sum(lista)
print(f'A soma desses números é: {soma}.')
mult = lista[0] * lista[1] * lista[2] * lista[3] * lista[4]
print(f'A multiplicação desses números é: {mult}.')
