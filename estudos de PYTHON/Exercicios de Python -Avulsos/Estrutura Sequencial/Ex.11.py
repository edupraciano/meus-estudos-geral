""" Ex.11 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
int1 = int(input('Digite o primeiro número INTEIRO: '))
int2 = int(input('Digite OUTRO número INTEIRO: '))
real = float(input('Digite um núm   ero REAL: '))

# RESPOSTA DA LETRA A
resA = (2 * int1) * (int2 / 2)
print(f'O resultado para a letra a) é: {resA:.2f}')

# RESPOSTA DA LETRA B
resB = 3 * int1 + real
print(f'O resultado para a letra b) é: {resB:.2f}')

# RESPOSTA DA LETRA C
resC = real ** 3
print(f'O resultado para a letra c) é: {resC:.2f}')
