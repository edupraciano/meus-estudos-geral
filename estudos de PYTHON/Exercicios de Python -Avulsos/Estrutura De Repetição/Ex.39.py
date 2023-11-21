""" Ex.39 Faça um programa que leia CINCO conjuntos de dois valores, o primeiro representando o nome do aluno e o
segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do
aluno mais alto e o nome do aluno mais baixo, com suas alturas."""

mais_alto = 0
mais_baixo = 100000  # Um número grande para garantir que qualquer altura inserida será menor
for i in range(5):
    aluno = str(input(f'Digite o código do {i + 1}º Aluno: '))
    altura = float(input(f'Digite a Altura do {i + 1}º Aluno: '))
    if altura > mais_alto:
        aluno_mais_alto = aluno
        mais_alto = altura
    if altura < mais_baixo:
        aluno_mais_baixo = aluno
        mais_baixo = altura

print(f'O aluno mais alto é o aluno {aluno_mais_alto} que tem {mais_alto:2.2f}m de altura.')
print(f'O aluno mais baixo é o aluno {aluno_mais_baixo} que tem {mais_baixo:2.2f}m de altura.')
