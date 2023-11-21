""" Ex.41 Faça um programa que receba o valor de uma dívida e a quantidade de parcelas a serem pagas. Mostre uma
tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros
e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas            % de Juros sobre o valor
                                     inicial da dívida
1                                            0
maior que 1 e menor ou igual a 3             10
maior que 3 e menor ou igual a 6             15
maior que 6 e menor ou igual a 12            20
maior que 12                                 25

Exemplo de saída do programa:

Valor da Dívida   Valor dos Juros    Quantidade de Parcelas        Valor da Parcela
R$ 1.000,00          0                       1                       R$  1.000,00
R$ 1.100,00          100                     3                       R$    366,00
R$ 1.150,00          150                     6                       R$    191,67
"""
divida = float(input('Qual o valor da  dívida? R$: '))
parcelas = int(input('Em quantas parcelas deseja pagar a dívida? '))
juros = 0
if parcelas == 1:
    juros = 0
elif 1 < parcelas <= 3:
    juros = 10 / 100
elif 3 < parcelas <= 6:
    juros = 15 / 100
elif 6 < parcelas <= 12:
    juros = 20 / 100
elif parcelas > 12:
    juros = 25 / 100

valor_divida = divida + (divida * juros)
valor_parcela = valor_divida / parcelas

print()
print('-=' * 60)
print(f'{"Simulação da Dívida":^110}')
print('-=' * 60)
print(f'{"Valor da Dívida (R$)":<30}   {"Percentual dos Juros (%)":<30} {"Qtde. de Parcelas":<30} {"Valor da Parcela (R$)":<30}')
print(f'R$ {valor_divida:>.2f} {juros * 100:>27.2f}  {parcelas:>25} {"R$":>31} {valor_parcela:>2.2f}')
