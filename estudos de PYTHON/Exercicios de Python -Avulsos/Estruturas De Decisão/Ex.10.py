""" Ex.10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
conforme o caso.
"""
turno = str(input('Qual Turno você estuda? [M-matutino | V-Vespertino | N- Noturno]: ')).strip().upper()[0]
if turno == 'M':
    print(f'\nBom Dia.')
elif turno =='V':
    print(f'\nBoa Tarde.')
elif turno == 'N':
    print(f'\nBoa Noite.')
else:
    print(f'\nValor Inválido.')
