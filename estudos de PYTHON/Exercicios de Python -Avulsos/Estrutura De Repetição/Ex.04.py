""" Ex.04 Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de
3% e que a população de B, seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento."""

# Inicializa as populações e taxas de crescimento
populacao_A = 80000
taxa_crescimento_A = 0.03
populacao_B = 200000
taxa_crescimento_B = 0.015

# Inicializa o contador de anos
anos = 0

# Loop até que a população do país A ultrapasse a população do país B
while populacao_A < populacao_B:
    # Atualiza as populações para o próximo ano
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    # Incrementa o contador de anos
    anos += 1

print(f'Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.')







