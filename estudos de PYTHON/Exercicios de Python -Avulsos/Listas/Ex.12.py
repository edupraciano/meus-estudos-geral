"""Ex.12 Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais
de 13 anos possuem altura inferior à média de altura desses alunos.
"""
idades = []
alturas = []
soma_altura = 0
cont_aluno_inferir_media = 0

for i in range(10):

    idade = int(input(f'Entre com a idade do {i + 1}º aluno: '))
    altura = float(input(f'Entre com a altura do {i + 1}º aluno: '))

    idades.append(idade)
    alturas.append(altura)
    soma_altura += altura

media = soma_altura / 10

for i in range(10):
    if idades[i] > 13 and alturas[i] < media:
        cont_aluno_inferir_media += 1

print(f'A média das alturas dos alunos é de {media}m')
print(f'Ao todo existem {cont_aluno_inferir_media} alunos com a altura a baixo da média e com idade superior a 13 anos.')

