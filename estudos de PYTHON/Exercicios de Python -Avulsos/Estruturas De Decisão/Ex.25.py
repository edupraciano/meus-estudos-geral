""" Ex.25 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- Telefonou para a vítima?
- Esteve no local do crime?
- Mora perto da vítima?
- Devia para a vítima?
- Já trabalhou com a vítima?
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
cont = 0
pergunta1 = str(input('Telefonou para a vítima? [S/N] ')).strip().upper()[0]
if pergunta1 == 'S':
    cont += 1
pergunta2 = str(input('Esteve no local do crime? [S/N] ')).strip().upper()[0]
if pergunta2 == 'S':
    cont += 1
pergunta3 = str(input('Mora perto da vítima? [S/N] ')).strip().upper()[0]
if pergunta3 == 'S':
    cont += 1
pergunta4 = str(input('Devia para a vítima? [S/N] ')).strip().upper()[0]
if pergunta4 == 'S':
    cont += 1
pergunta5 = str(input('Já trabalhou com a vítima? [S/N] ')).strip().upper()[0]
if pergunta5 == 'S':
    cont += 1

if cont == 2:
    print('\nPessoa Suspeita!')
elif cont == 3 or cont == 4:
    print('\nCúmplice!')
elif cont == 5:
    print('\nAssassino!')
elif cont == 1 or cont == 0:
    print('\nInocente!')


