""" Ex.27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:
            Até 5 k | Acima de 5 kg
Morango R$ 2,50 por | kg R$ 2,20 por kg
Banana  R$ 1,80 por | kg R$ 1,50 por kg

Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em kg) de morangos e a quantidade (em kg) de Banana
adquiridas e escreva o valor a ser pago pelo cliente.
"""
while True:
    fruta = str(input('Qual Fruta você irá comprar? [M-Morango | B-Banana]: ')).strip().upper()[0]
    if fruta in "MB":
        break
    print('Entrada inválida. Por favor, digite M para Morango ou B para Banana.')

while True:
    entrada = input(f'Quantos Kg de {fruta} você comprar? ')
    if entrada.replace('.', '', 1).isdigit():
        peso = float(entrada)
        break
    print('Entrada inválida. Por favor, digite um número.')

if fruta == 'M' and peso <= 5:
    preço = 2.5
elif fruta == 'M' and peso > 5:
    preço = 2.2
elif fruta == 'B' and peso <= 5:
    preço = 1.8
elif fruta == 'B' and peso > 5:
    preço = 1.5

valor_sem_desconto = preço * peso

if peso > 8 or valor_sem_desconto >= 25:
    desconto = valor_sem_desconto * 0.1
    valor_com_desconto = valor_sem_desconto - desconto
    print('-=' * 70)
    print(f'Como foram comprados mais de 8Kg de frutas ou o valor que foi pago foi superior a R$ 25,00, '
          f'será concedido um desconto de 10%\nem cima do valor sem desconto de R$ {valor_sem_desconto:.2f} '
          f'o que representa uma economia de R$ {desconto:.2f}. '
          f'O novo valor a ser pago será de R$ {valor_com_desconto:.2f}.'
          f'\nObrigado e volte sempre!')
    print('-=' * 70)
else:
    print('-=' * 70)
    print(f'O Valor sem desconto para {peso} kg de {"Morangos" if fruta == "M" else "Bananas"} é de R$ {valor_sem_desconto:.2f}.'
          f'\nObrigado e volte sempre!')
    print('-=' * 70)
