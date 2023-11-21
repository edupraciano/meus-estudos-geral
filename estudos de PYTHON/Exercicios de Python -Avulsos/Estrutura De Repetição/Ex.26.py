""" Ex.26 Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
eleitor votar e ao final mostrar o número de votos de cada candidato."""
N = int(input('Quantos eleitores existem? '))
A = B = C = cont = 0
print('Escolha entre os seguintes candidatos: [A , B ou C]')
for n in range(1, N + 1):
    voto = str(input(f'Em qual Candidato você votará o {cont + 1}º eleitor?: ')).strip().upper()[0]
    cont += 1
    if voto == 'A':
        A += 1
    elif voto == 'B':
        B += 1
    elif voto == 'C':
        C += 1


print(f'\nEstes foram os votos: \n{A} votos para o Candidato A, \n{B} votos para o Candidato B \n{C} votos para o Candidato C.')