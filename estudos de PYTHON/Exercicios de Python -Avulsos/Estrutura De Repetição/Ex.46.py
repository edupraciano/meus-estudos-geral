""" Ex.46 Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos
de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
calcular a média). Use uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do
programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

while True:
    saltos = []
    atleta = str(input('Qual o nome do atleta? ')).strip().upper()
    for i in range(5):
        salto = float(input(f'Informe o {i + 1} salto: '))
        saltos.append(salto)

    print()
    print('-=' * 30)
    print(f'Atleta: {atleta}')
    print()
    print(f'Primeiro salto: {saltos[0]:.2f} m')
    print(f'Segundo salto: {saltos[1]:.2f} m')
    print(f'Terceiro salto: {saltos[2]:.2f} m')
    print(f'Quarto salto: {saltos[3]:.2f} m')
    print(f'Quinto salto: {saltos[4]:.2f} m')

    menor_salto = min(saltos)
    saltos.remove(menor_salto)
    maior_salto = max(saltos)
    saltos.remove(maior_salto)
    media = sum(saltos) / 3

    print(f'O MELHOR salto foi {maior_salto:.2f} m;')
    print(f'O PIOR salto foi {menor_salto:.2f} m;')
    print(f'Descartados o maior e o menor salto, os saltos válidos são : {saltos}')

    print()
    print('Resultado Final')
    print(f'{atleta}: {media:.2f} m')
    print('-=' * 30)
    print()

    while True:
        sair = str(input('Deseja SAIR? [S/N]: ')).strip().upper()[0]
        if sair in "S/N":
            break
        else:
            print('Entrada Inválida. Digite S para SAIR ou N para continuar.')

    if sair == 'S':
        break

print('Programa Encerrado!')
