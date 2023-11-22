# Ex.11 Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
lista_A = []
lista_B = []
lista_C = []
lista_D = []

# Lendo os 10 elementos da lista A
for a in range(10):
    num_A = int(input(f'Entre com o {a + 1}º número da lista A: '))
    lista_A.append(num_A)

# Lendo os 10 elementos da lista B
for b in range(10):
    num_B = int(input(f'Entre com o {b + 1}º número da lista B: '))
    lista_B.append(num_B)

# Lendo os 10 elementos da lista C
for c in range(10):
    num_C = int(input(f'Entre com o {c + 1}º número da lista C: '))
    lista_C.append(num_C)

# Intercalando os elementos das listas A, B e C para formar a lista D
for i in range(10):
    lista_D.append(lista_A[i])
    lista_D.append(lista_B[i])
    lista_D.append(lista_C[i])

print(f'A lista_A é: {lista_A}')
print(f'A lista_B é: {lista_B}')
print(f'A lista_C é: {lista_C}')
print(f'A lista_D intercalada é: {lista_D}')

