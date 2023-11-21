"""Ex.06 Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0. """
lista_de_medias = []
lista_de_alunos_medias_maiores7 = []
media_maior7 = 0

for a in range(10):

    aluno = input(f'Qual o nome do {a + 1} Aluno?: ').upper().strip()

    soma_nota = 0

    for n in range(4):
        nota = int(input(f'Digite {n + 1}ª nota do aluno {aluno}: '))
        soma_nota += nota

    media = soma_nota / 4

    if media >= 7:
        media_maior7 += 1
        lista_de_alunos_medias_maiores7.append(aluno)

    lista_de_medias.append(media)

print(f'Ao todo {media_maior7} alunos tiveram média 7 ou superior, são eles: ', end='')
print(lista_de_alunos_medias_maiores7)
