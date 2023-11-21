""" Ex.25 Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de
idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada."""
cont = soma = 0

while True:
    idade = int(input(f'Digite a idade da {cont + 1}ª pessoa: '))
    soma += idade
    cont += 1

    sair = ''
    while sair not in ['S', 'N']:
        sair = input('Deseja SAIR? [S/N]: ').strip().upper()[0]

        if sair not in ['S', 'N']:
            print('Entrada inválida. Digite apenas S ou N.')

    if sair == 'S':
        break

media = soma / cont

if 0 < media <= 25:
    turma = 'Jovem'
elif 26 <= media <= 60:
    turma = 'Adulta'
elif media > 60:
    turma = 'Idosa'

print(f'\nPara essas idades, podemos considerar a turma como sendo "{turma}"'
      f'com uma média de idade de {media:.2f} anos.')
