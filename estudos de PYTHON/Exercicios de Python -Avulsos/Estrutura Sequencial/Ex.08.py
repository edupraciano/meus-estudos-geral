""" Ex.08 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
valor_por_hora = float(input('Quanto você ganha por hora trabalhada? '))
qtde_horas_mes = int(input('Quantas horas você trabalha no mÊs? '))
salario = valor_por_hora * qtde_horas_mes

print(f'O seu salário é de R$ {salario:.2f}')
