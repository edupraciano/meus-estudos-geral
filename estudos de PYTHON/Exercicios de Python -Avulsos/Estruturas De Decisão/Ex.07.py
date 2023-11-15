# Ex.07 Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = menor = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite Outro número: '))
n3 = int(input('Digite MAIS um Outro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    print(f'\nO maior dos números digitados foi: {maior}.')
elif n2 > n1 and n2 > n3:
    maior = n2
    print(f'\nO maior dos números digitados foi: {maior}.')
else:
    maior = n3
    print(f'\nO maior dos números digitados foi: {maior}.')

if n1 < n2 and n1 < n3:
    menor = n1
    print(f'O menor dos números digitados foi: {menor}.')
elif n2 < n1 and n2 < n3:
    menor = n2
    print(f'O menor dos números digitados foi: {menor}.')
else:
    menor = n3
    print(f'O menor dos números digitados foi: {menor}.')