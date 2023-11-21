""" Ex.06 Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa
para que ele mostre os números um ao lado do outro."""
cont = 0
while cont <= 20:
    print(cont)
    cont += 1

cont = 0
while cont <= 20:
    print(f' > {cont}', end='')
    cont += 1
