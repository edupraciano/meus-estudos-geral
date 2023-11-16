""" Ex.21 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
    informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
    O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
    existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
"""
print('\nO valor deve estar entre R$ 10,00 e R$ 600,00')
valor_saque = int(input('Qual o valor do Saque? R$: '))
print()
falta = 0

if 10 <= valor_saque <= 600:

    if valor_saque >= 100:
        ced_de_100 = valor_saque // 100
        falta = valor_saque - ced_de_100 * 100
        print(f'Serão liberadas {ced_de_100} notas de R$ 100,00.')

    if falta >= 50:
        ced_de_50 = falta // 50
        falta = falta - ced_de_50 * 50
        print(f'Serão liberadas {ced_de_50} notas de R$ 50,00.')

    if falta >= 10:
        ced_de_10 = falta // 10
        falta = falta - ced_de_10 * 10
        print(f'Serão liberadas {ced_de_10} notas de R$ 10,00.')

    if falta >= 5:
        ced_de_5 = falta // 5
        falta = falta - ced_de_5 * 5
        print(f'Serão liberadas {ced_de_5} notas de R$ 5,00 .')

    if falta >= 1:
        ced_de_1 = falta // 1
        print(f'Serão liberadas {ced_de_1} notas de R$ 1,00.')

else:
    print('\nO valor deve estar entre R$ 10,00 e R$ 600,00')

