"""Ex.17 Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
while True:
    atleta = input('Entre com o nome do atleta (ou digite "sair" para encerrar): ')

    if atleta.lower() == "sair":
        break

    saltos = []

    for s in range(5):
        salto = float(input(f'Entre com o {s + 1}º salto: '))
        saltos.append(salto)

    # Remover o maior e o menor salto
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))

    media = sum(saltos) / 3

    print(f'\nResultado final:')
    print(f'Atleta: {atleta}')
    print(f'Saltos: {saltos}')
    print(f'Média dos saltos: {media:.2f} m\n')
