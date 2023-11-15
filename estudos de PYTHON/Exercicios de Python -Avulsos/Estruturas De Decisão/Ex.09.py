# Ex.09 Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite O PRIMEIRO número: '))
n2 = int(input('Digite O SEGUNDO número: '))
n3 = int(input('Digite O TERCEIRO número: '))

primeiro = segundo = terceiro = 0

if n1 < n2 and n1 < n3:
    primeiro = n1
    if n2 < n3:
        segundo = n2
        terceiro = n3

elif n2 < n1 and n2 < n3:
    primeiro = n2
    if n1 < n3:
        segundo = n1
        terceiro = n3

elif n3 < n1 and n3 < n2:
    primeiro = n3
    if n1 < n2:
        segundo = n1
        terceiro = n2

print(f'\nOs números em ordem DECRESCENTE é: {terceiro}, {segundo}, {primeiro}')
