# Ex.07 Faça um programa que leia 5 números e informe o maior número.
maior = cont = 0
for c in range(1, 6):
    num = float(input(f'Digite o {c}º número: '))
    if c == 1 or num > maior:
        maior = num
        cont = c
print(f'O maior número digitado foi: {maior} e ele foi digitado na {cont}ª posição')
