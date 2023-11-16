""" Ex.26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
-- Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
-- Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G- gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90.
"""
while True:
    entrada = input('Quantos litros foram abastecidos? ')
    if entrada.isdigit():
        litros = int(entrada)
        break
    print('Digite a quantidade de litros que foram abastecidos.')

while True:
    entrada = input('Qual o tipo de combustível foi colocado? [G/A] ').strip().upper()[0]
    if entrada.isalpha() and entrada in 'AG':
        tipo = str(entrada)
        break
    print('Digite G para Gasolina ou A para Álcool')

valor_gas = 2.5
valor_alc = 1.9

# Para a GASOLINA
if tipo == 'G':

    total_cheio = litros * valor_gas

    if litros <= 20:
        desconto = total_cheio * 0.04
        valor_pago_com_desconto = total_cheio - desconto
        print()
        print('-=' * 87)
        print(f'Para {litros} litro de Gasolina, o valor sem desconto seria de R$ {total_cheio:.2f}. '
              f'Porém como foram abastecidos {litros} litros, você recebeu 4% de desconto\npor litro o que representa'
              f'uma economia de R$ {desconto:.2f} e o valor a ser pago fica em R$ {valor_pago_com_desconto:.2f}.')
        print('-=' * 87)
    elif litros > 20:
        desconto = total_cheio * 0.06
        valor_pago_com_desconto = total_cheio - desconto
        print()
        print('-=' * 70)
        print(f'Para {litros} litro de Gasolina, o valor sem desconto seria de R$ {total_cheio:.2f}. '
              f'Porém como foram abastecidos {litros} litros, você recebeu 6% de desconto\npor litro o que representa'
              f'uma economia de R$ {desconto:.2f} e o valor a ser pago fica em R$ {valor_pago_com_desconto:.2f}.')
        print('-=' * 70)

# Para a ÁLCOOL
elif tipo == 'A':

    total_cheio = litros * valor_alc

    if litros <= 20:
        desconto = total_cheio * 0.03
        valor_pago_com_desconto = total_cheio - desconto
        print()
        print('-=' * 70)
        print(f'Para {litros} litro de Álcool, o valor sem desconto seria de R$ {total_cheio:.2f}. '
              f'Porém como foram abastecidos {litros} litros, você recebeu 3% de desconto\npor litro o que representa'
              f'uma economia de R$ {desconto:.2f} e o valor a ser pago fica em R$ {valor_pago_com_desconto:.2f}.')
        print('-=' * 70)
    elif litros > 20:
        desconto = total_cheio * 0.05
        valor_pago_com_desconto = total_cheio - desconto
        print()
        print('-=' * 70)
        print(f'Para {litros} litro de Gasolina, o valor sem desconto seria de R$ {total_cheio:.2f}. '
              f'Porém como foram abastecidos {litros} litros, você recebeu 5% de desconto\npor litro o que representa'
              f'uma economia de R$ {desconto:.2f} e o valor a ser pago fica em R$ {valor_pago_com_desconto:.2f}.')
        print('-=' * 70)
