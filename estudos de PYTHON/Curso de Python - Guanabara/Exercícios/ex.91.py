"""
Ex. 91 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador_01': randint(1, 6),
        'Jogador_02': randint(1, 6),
        'Jogador_03': randint(1, 6),
        'Jogador_04': randint(1, 6), }

ranking = []
print(f' {"  == Valores Sorteados  ==  ":^30} ')
print('-=' * 20)
for k, v in jogo.items():
    print(f'{k} tirou o número: {v}')
    sleep(1)
print()
print(f' {"Ranking dos Jogadores":^30} ')
print('-=' * 20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{int(i) + 1}º lugar é o {v[0]} com {v[1]} pontos.')
    sleep(1)
print(f'\nFinalizando...')
