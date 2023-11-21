""" Ex.27 Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e
a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""
total_alunos = 0
qtde_turmas = int(input('Qual a quantidade de turmas? '))
for i in range(qtde_turmas):
    qtde_alunos = int(input(f'Qual a quantidade de alunos da {i + 1}ª turma? '))

    while qtde_alunos > 40:
        print(f'Quantidade de Alunos excedida para a {i + 1}ª turma. Não mais de 40 Alunos por turma.')
        qtde_alunos = int(input(f'Qual a quantidade de alunos da {i + 1}ª turma? '))

    total_alunos += qtde_alunos

media = total_alunos / qtde_turmas

print(f'\nA média de alunos por turma é de: {media:.2f}.')