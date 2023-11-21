""" Ex.30 O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
que já é um sucesso na loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços
de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""
qtde_paes = int(input('Quantos pães serão comprados? '))
total = 0
for i in range(qtde_paes):
    preço_pão = float(input(f'Qual o preço da unidade do {i + 1}º pão? '))
    total += preço_pão
print(f'\nPara {(i + 1)} {"Pão" if i == 0  else "pães"} o valor pago será de R$ {total:.2f}')

