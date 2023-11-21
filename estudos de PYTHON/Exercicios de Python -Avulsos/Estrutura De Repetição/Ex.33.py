""" Ex.33 O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia uma quantidade
indeterminada de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas."""
cont = 1
menor = maior = soma = 0
print('[ DIGITE 0 (ZERO) PARA SAIR ]')
while True:
    temperatura = float(input(f'Digite a {cont}ª temperatura: '))
    if temperatura == 0:
        break
    elif cont == 1:
        maior = menor = temperatura
        soma += temperatura
    elif temperatura > maior:
        maior = temperatura
        soma += temperatura
    elif temperatura < menor:
        menor = temperatura
        soma += temperatura
    cont += 1

media = soma / (cont - 1)

print(f'\nForam aferidas {cont} temperaturas e seus valores são...')
print(f'A maior temperatura registrada foi de {maior:.2f}ºC')
print(f'A menor temperatura registrada foi de {menor:.2f}ºC')
print(f'A media das temperaturas registradas foi de {media:.2f}ºC')