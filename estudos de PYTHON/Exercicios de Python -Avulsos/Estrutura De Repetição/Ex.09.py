# Ex.09 Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for n in range(50):
    if n % 2 != 0:
        print(f' > {n}', end='')
