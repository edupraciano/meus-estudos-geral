"""Ex.10 Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
lista_A = []
lista_B = []
lista_C = []

# Lendo os 10 elementos da lista A
for a in range(10):
    num_A = int(input(f'Entre com o {a + 1}º número da lista A: '))
    lista_A.append(num_A)

# Lendo os 10 elementos da lista B
for b in range(10):
    num_B = int(input(f'Entre com o {b + 1}º número da lista B: '))
    lista_B.append(num_B)

# Intercalando os elementos das listas A e B para formar a lista C
for i in range(10):
    lista_C.append(lista_A[i])
    lista_C.append(lista_B[i])

print(f'A lista_A é: {lista_A}')
print(f'A lista_B é: {lista_B}')
print(f'A lista_C intercalada é: {lista_C}')
