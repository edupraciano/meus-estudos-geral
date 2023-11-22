"""Ex.09 Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor.
"""
lista = []
for i in range(10):
    num = int(input(f'Digite o {i + 1}º número: '))
    lista.append(num)

ele0 = lista[0] * lista[0]
ele1 = lista[1] * lista[1]
ele2 = lista[2] * lista[2]
ele3 = lista[3] * lista[3]
ele4 = lista[4] * lista[4]
ele5 = lista[5] * lista[5]
ele6 = lista[6] * lista[6]
ele7 = lista[7] * lista[7]
ele8 = lista[8] * lista[8]
ele9 = lista[9] * lista[9]

soma_dos_quadrados = ele0 + ele1 + ele2 + ele3 +ele4 + ele5 + ele6 + ele7 + ele8 + ele9
print()
print(f'A soma dos quadrados dos elementos da lista é: {soma_dos_quadrados}')
