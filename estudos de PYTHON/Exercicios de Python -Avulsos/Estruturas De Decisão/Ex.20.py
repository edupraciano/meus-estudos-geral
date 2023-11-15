""" Ex.20 Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a
    média alcançada por aluno e presentar:
a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""
aluno = input('\nQual o nome do aluno(a) ? ')
nota1 = float(input(f'Qual a PRIMEIRA nota de {aluno}? '))
nota2 = float(input(f'Qual a SEGUNDA nota de {aluno}? '))
nota3 = float(input(f'Qual a TERCEIRA nota de {aluno}? '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f'\nO aluno {aluno} foi APROVADO com a média {media:.2f}.')
elif media < 7:
    print(f'\nO aluno {aluno} foi REPROVADO com a média {media:.2f}.')
elif media == 10:
    print(f'\nO aluno {aluno} foi APROVADO COM DISTINÇÃO com a média {media:.2f}.')