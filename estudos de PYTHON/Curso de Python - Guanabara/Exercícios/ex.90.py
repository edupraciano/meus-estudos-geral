"""
Ex.90 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >=3 and aluno['média']:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():    
    print(f'  -- {k} é igual a {v}')
