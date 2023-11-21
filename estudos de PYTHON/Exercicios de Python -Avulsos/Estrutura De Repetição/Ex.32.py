""" Ex.32 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo: Fatorial de: 5 5! =  5 . 4 . 3 . 2 . 1 = 120"""

num = int(input('Digite o número que quer ver o fatorial: '))
fat = 1
fatorial_str = ""

for i in range(num, 0, -1):
    fat *= i
    if i == num:
        fatorial_str += str(i)
    else:
        fatorial_str += " x " + str(i)

print(f'{num}! = {fatorial_str} = {fat}')