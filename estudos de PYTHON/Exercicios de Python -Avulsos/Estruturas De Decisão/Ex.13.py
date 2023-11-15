""" Ex.13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido.
"""
entrada = int(input('\nDigite um número de 1 a 7 para descobrir um dia da semana: '))
dias = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']
if entrada == 0:
    print('\nDomingo')
elif entrada == 1:
    print('\nSegunda-Feira')
elif entrada == 2:
    print('\nTerça-feira')
elif entrada == 3:
    print('\nQuarta-feira')
elif entrada == 4:
    print('\nQuinta-feira')
elif entrada == 5:
    print('\nsexta-feira')
elif entrada == 6:
    print('\nSábado')
else:
    print('\nEntrada ínválida!')
