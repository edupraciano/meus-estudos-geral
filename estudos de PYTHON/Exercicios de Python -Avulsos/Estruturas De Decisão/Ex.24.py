""" Ex.24 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
(somar, subtrair, multiplicar ou dividir). O resultado da operação deve ser acompanhado de uma frase que diga se
o número é:
a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal.
"""
num1 = int(input('Digite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
res = 0

print('''
[1] Somar
[2] Subtrair
[3] Multiplica
[4] Dividir''')

while True:
    op = input('\nQual operação deseja realizar os esse número? ')

    if op not in '1234':
        print('Digite qual operação você deseja realizar')
        print('''
        [1] Somar
        [2] Subtrair
        [3] Multiplica
        [4] Dividir''')
    else:
        if op == '1':
            res = num1 + num2
            print(f'A Soma entre os número {num1} e {num2} é {res}')
            print('-=' * 30)
        elif op == '2':
            res = num1 - num2
            print(f'A Subtração entre os número {num1} e {num2} é {res}')
            print('-=' * 30)
        elif op == '3':
            res = num1 * num2
            print(f'A Multiplicação entre os número {num1} e {num2} é {res}')
            print('-=' * 30)
        elif op == '4':
            if num2 != 0:
                res = num1 / num2
                print(f'A Divisão entre os número {num1} e {num2} é {res}')
                print('-=' * 30)
            else:
                print('Não é possível a divisão por 0')
                print('-=' * 30)

        while True:
            sair = str(input(f'Deseja SAIR? [S/N] ')).strip().upper()[0]
            if sair in 'SN':
                break
            else:
                print('Digite S para SAIR ou N para continuar.')

        if sair == 'S':
            break

print('-=' * 30)
print('\nPrograma Encerrado!')
