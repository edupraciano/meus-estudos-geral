""" Ex.44 Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são: 1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/
2- João/etc) 5 - Voto Nulo 6 - Voto em Branco
Faça um programa que calcule e mostre:
a) O total de votos para cada candidato;
b) O total de votos nulos;
c) O total de votos em branco;
d) A percentagem de votos nulos sobre o total de votos;
e) A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""
print()
print("""[ 1 ] - João Filho
[ 2 ] - Marcos Pontes
[ 3 ] - Maria do Carmo
[ 4 ] - Miguel dos Anjos
[ 5 ] - Voto Nulo
[ 6 ] - Voto em Branco""")
print()
votos_candidato1 = votos_candidato2 = votos_candidato3 = votos_candidato4 = votos_nulo = votos_branco = total = 0


while True:

    voto = int(input('Digite o seu voto: '))

    if voto == 0:
        break

    elif voto == 1:
        candidato = 'João Filho'
        votos_candidato1 += 1
        total += 1
    elif voto == 2:
        candidato = 'Marcos Pontes'
        votos_candidato2 += 1
        total += 1
    elif voto == 3:
        candidato = 'Maria do Carmo'
        votos_candidato3 += 1
        total += 1
    elif voto == 4:
        candidato = 'Miguel dos Anjos'
        votos_candidato4 += 1
        total += 1
    elif voto == 5:
        candidato = 'Votos Nulo'
        votos_nulo += 1
        total += 1
    elif voto == 6:
        candidato = 'Votos em Branco'
        votos_branco += 1
        total += 1

print()
print('-=' * 25)
print(f'Ao todo foram contabilizados {total} votos.')

print('-=' * 25)
# a) O total de votos para cada candidato;
print(f'Votos para João Filho: {votos_candidato1}')
print(f'Votos para Marcos Pontes: {votos_candidato2}')
print(f'Votos para Maria do Carmo: {votos_candidato3}')
print(f'Votos para Miguel dos Anjos: {votos_candidato4}')

# b) O total de votos nulos;
print(f'Votos nulos: {votos_nulo}')

# c) O total de votos em branco;
print(f'Votos em branco: {votos_branco}')

print('-=' * 25)
# d) A percentagem de votos nulos sobre o total de votos;
percentual_nulo = votos_nulo / total
print(f'O percentual de votos nulo foi de {percentual_nulo * 100:.2f} %.')

# e) A percentagem de votos em branco sobre o total de votos
percentual_branco = votos_branco / total
print(f'O percentual de votos nulo foi de {percentual_branco * 100:.2f} %.')
