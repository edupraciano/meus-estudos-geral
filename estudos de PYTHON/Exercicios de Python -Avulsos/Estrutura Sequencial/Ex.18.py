""" Ex.18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho = float(input('Qual o tamanho do arquivo em MB?: '))
velocidade = float(input('Qual a velocidade de transmissão em Mbps?: '))

tempo_em_minutos = tamanho / velocidade * 60
print(f'{tempo_em_minutos} min')
