# Ex.02 Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    num = int(input(f'Entre com o {i + 1}º Número: '))
    lista.append(num)
print(f'A lista na ordem de entrada é {lista}')
lista.reverse()
print(f'A lista na ordem inversa é {lista}')


