"""Ex.13 Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
               'Novembro', 'Dezembro']
lista_temperaturas = []
meses_acima_media = []
soma = 0
for m in range(12):

    temperatura_media = float(input(f'Entre com a temperatura de {lista_meses[m]}: '))
    lista_temperaturas.append(temperatura_media)
    soma += temperatura_media

media = soma / 12

for i in range(12):
    if lista_temperaturas[i] > media:
        meses_acima_media.append(lista_meses[i])

print(f'Estes foram os meses com temperaturas acima da média de {media:.2f}ºC: {meses_acima_media}.')

