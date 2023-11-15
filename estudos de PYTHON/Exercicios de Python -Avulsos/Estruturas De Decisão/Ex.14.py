""" Ex.14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à 	tabela abaixo:
Média de Aproveitamento   Conceito
Entre 9.0 e 10.0             A
Entre 7.5 e 9.0              B
Entre 6.0 e 7.5              C
Entre 4.0 e 6.0              D
Entre 4.0 e zero             E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se
o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
nota1 = int(input('Entre com a Primeira nota [0 - 10]: '))
nota2 = int(input('Entre com a Segunda nota [0 - 10]: '))
media = (nota1 + nota2) / 2
if 9 < media <= 10:
    print(f'\nCom as notas {nota1} e {nota2} o aluno fico com a média {media:.2f} e seu conceito é A.')
    print('Por tanto o aluno foi APROVADO.')
elif 7.5 < media <= 9:
    print(f'\nCom as notas {nota1} e {nota2} o aluno fico com a média {media:.2f} e seu conceito é B.')
    print('Por tanto o aluno foi APROVADO.')
elif 6 < media <= 7.5:
    print(f'\nCom as notas {nota1} e {nota2} o aluno fico com a média {media:.2f} e seu conceito é C.')
    print('Por tanto o aluno foi APROVADO.')
elif 4 < media <= 6:
    print(f'\nCom as notas {nota1} e {nota2} o aluno fico com a média {media:.2f} e seu conceito é D.')
    print('Por tanto o aluno foi REPROVADO.')
elif 0 <= media <= 4:
    print(f'\nCom as notas {nota1} e {nota2} o aluno fico com a média {media:.2f} e seu conceito é E.')
    print('Por tanto o aluno foi REPROVADO.')


