""" Ex.05 Faça um programa que leia o nome do aluno e duas notas parciais obtidas por ele em uma
    disciplina ao longo de um semestre e que apresente a média e informe se o aluno está Aprovado, Em Recuperação
    ou Reprovado a depender dos critérios a seguir:
 - nota 10: Aluno Aprovado Com Louvor;
 - nota maior ou igual a 7 e menor do que 10: Aluno Aprovado;
 - nota maior ou igual a 4 e menor do que 7: Aluno em Recuperação;
 - nota menor do que 4: Aluno Reprovado;
"""
aluno = str(input('Digite o nome do Aluno: '))
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))

media = (n1 + n1) / 2

if media == 10:
    print('-=' * 50)
    print(f'Com as notas {n1} e {n2} o Aluno(a): {aluno} ficou com a média {media} e está Aprovado Com Louvor')
    print('-=' * 50)
elif 10 > media >= 7:
    print('-=' * 50)
    print(f'Com as notas {n1} e {n2} o Aluno(a): {aluno} ficou com a média {media} e está Aprovado.')
    print('-=' * 50)
elif 7 > media >= 4:
    print('-=' * 50)
    print(f'Com as notas {n1} e {n2} o Aluno(a): {aluno} ficou com a média {media} e está em Recuperação.')
    print('-=' * 50)
elif media < 4:
    print('-=' * 50)
    print(f'Com as notas {n1} e {n2} o Aluno(a): {aluno} ficou com a média {media} e está Reprovado.')
    print('-=' * 50)
