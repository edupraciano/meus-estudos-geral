""" Ex.19 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input("Digite um número menor do que mil: "))
num_string = str(num)

if num == 0:
    print('Você digitou o número ZERO.')
elif num < 0:
    print('Você digitou um número negativo, ENTRADA INVÁLIDA!')
elif (len(num_string)) == 3:
    unidade = num_string[-1]
    dezenas = num_string[-2]
    centena = num_string[-3]
    print(f'O número {num} = {centena} centenas, {dezenas} dezenas e {unidade} unidades')
elif (len(num_string)) == 2:
    unidade = num_string[-1]
    dezenas = num_string[-2]
    print(f'O número {num} = {dezenas} dezenas e {unidade} unidades')
elif (len(num_string)) == 1 and (len(num_string)) != 0:
    unidade = num_string[-1]
    print(f'O número {num} = Só é composto de somente {unidade} unidades')


