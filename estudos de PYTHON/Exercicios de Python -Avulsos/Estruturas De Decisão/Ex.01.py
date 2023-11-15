# Ex.01 Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite Outro número: '))
maior = menor = 0
if n1 > n2:
    maior = n1
else:
    maior = n2
print(f'\nO maior dos números digitados foi {maior}.')