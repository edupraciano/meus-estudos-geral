""" Ex.36 Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""

num = int(input('Digite o número que vc quer ver a tabuada: '))
inicio = int(input('Digite o número que vc quer INICIAR a tabuada: '))
final = int(input('Digite o número que vc quer FINALIZAR a tabuada: '))

if final <= inicio:
    print('Não é possível montar a tabuada, pois o número final é menor do que o inicial.')
else:
    print()
    print(f'Montar a tabuada de: {num}')
    print(f'Começar por: {inicio}')
    print(f'Terminar em: {final}')
    print(f'Vou montar a tabuada de {num} começando em {inicio} e terminando {final}. ')
    print()

    for i in range(inicio, final + 1):
        print(f'{num} x {i} = {num * i}')