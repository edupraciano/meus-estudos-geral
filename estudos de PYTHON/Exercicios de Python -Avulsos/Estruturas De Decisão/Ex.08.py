""" Ex.08 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
"""
produto1 = int(input('Quanto custa o primeiro produto? R$ '))
produto2 = int(input('Quanto custa o segundo produto? R$ '))
produto3 = int(input('Quanto custa o terceiro produto? R$ '))
mais_barato = ''
if produto1 < produto2 and produto1 < produto3:
    mais_barato = produto1
    print(f'\nDos três produtos o pesquisados, o mais barato é Primeiro produto que custa R$ {mais_barato:.2f}.')
elif produto2 < produto1 and produto2 < produto3:
    mais_barato = produto2
    print(f'\nDos três produtos o pesquisados, o mais barato é Segundo produto que custa R$ {mais_barato:.2f}.')
else:
    mais_barato = produto3
    print(f'\nDos três produtos o pesquisados, o mais barato é Terceiro produto que custa R$ {mais_barato:.2f}.')

