# Ex.06 Faça um Programa que leia três números e mostre o maior deles.
maior = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite Outro número: '))
n3 = int(input('Digite MAIS um Outro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    primeiro = 'PRIMEIRO - N1'
    print(f'\nO maior dos números digitados foi O {primeiro} que foi o número: {maior}.')
elif n2 > n1 and n2 > n3:
    maior = n2
    primeiro = 'SEGUNDO - N2'
    print(f'\nO maior dos números digitados foi O {primeiro} que foi o número: {maior}.')
else:
    maior = n3
    primeiro = 'TERCEIRO - N3'
    print(f'\nO maior dos números digitados foi O {primeiro} que foi o número: {maior}.')

