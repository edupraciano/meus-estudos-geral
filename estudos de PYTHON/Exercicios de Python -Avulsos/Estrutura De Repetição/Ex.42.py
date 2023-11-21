""" Ex.42 Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão
nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um
número negativo."""
num = 0
intervalo1 = intervalo2 = intervalo3 = intervalo4 = 0
while True:
    num = int(input('Digite um número: '))

    if num < 0:
        break
    else:
        if 0 <= num <= 25:
            intervalo1 += 1
        elif 26 <= num <= 50:
            intervalo2 += 1
        elif 51 <= num <= 75:
            intervalo3 += 1
        elif 76 <= num <= 100:
            intervalo4 += 1


print(f'Para os números que foram inseridos, {intervalo1} estão no intervalo: [0-25], {intervalo2} '
      f'estão no intervalo: [26-50], {intervalo3} estão no intervalo:  [51-75] e {intervalo4} '
      f'estão no intervalo:  [76-100].')
print('Programa Encerrado!')
