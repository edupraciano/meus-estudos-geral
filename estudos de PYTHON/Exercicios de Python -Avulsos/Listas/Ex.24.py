"""Ex.24 Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um
vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função
para gerar números aleatórios, simulando os lançamentos dos dados."""
import random

resultados = []
face1 = []
face2 = []
face3 = []
face4 = []
face5 = []
face6 = []

for i in range(100):

    jogada = random.randint(1, 6)
    resultados.append(jogada)

    if jogada == 1:
        face1.append(jogada)
    elif jogada == 2:
        face2.append(jogada)
    elif jogada == 3:
        face3.append(jogada)
    elif jogada == 4:
        face4.append(jogada)
    elif jogada == 5:
        face5.append(jogada)
    elif jogada == 6:
        face6.append(jogada)

print(f'O número 1 foi lançado {len(face1)} vezes.')
print(f'O número 2 foi lançado {len(face2)} vezes.')
print(f'O número 3 foi lançado {len(face3)} vezes.')
print(f'O número 4 foi lançado {len(face4)} vezes.')
print(f'O número 5 foi lançado {len(face5)} vezes.')
print(f'O número 6 foi lançado {len(face6)} vezes.')
