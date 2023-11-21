# Ex.17 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Digite um número para calcular o fatorial: '))
fat = 1
fatorial_str = ""
for i in range(num, 0, -1):
    fat *= i
    if i == 1:
        fatorial_str += str(i)
    else:
        fatorial_str += str(i) + " X "
print(f'Fatorial de {num}! \n{num}! = {fatorial_str} = {fat}')
