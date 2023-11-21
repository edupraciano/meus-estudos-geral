# Ex.03 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(4):
    nota = float(input(f'Entre com a {i + 1}ª nota: '))
    notas.append(nota)

media = sum(notas) / 4

print(f'A média das notas é: {media}')
