""" Ex.15 Faça um programa que pergunte quanto você ganha por hora o número de horas trabalhadas no mês.
Calcule o mostre o total do salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda
8% para o INSS e 5% para o sindicato, faça um programa que nos informe:
a) Salário Bruto;
b) Quanto pagou de INSS;
c) Quanto pagou ao sindicato;
d) Salário Líquido;
e) Calcule os descontos conforme a tabela abaixo:
+ Salário Bruto R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$
= Salário Líquido: R$
Obs.: Salário Líquido = Salário Bruto - Descontos
"""
hora_de_trabalho = float(input('Quanto vc ganha por hora trabalhada?: '))
qtde_de_horas_trabalhadas = float(input('Quantas horas vc trabalhou no mês?: '))
salario_bruto = hora_de_trabalho * qtde_de_horas_trabalhadas
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
descontos = (inss + ir + sindicato)
salario_liquido = salario_bruto - descontos
print()
print(f' (+) Salário Bruto: ------- R$ {salario_bruto:>8.2f}')
print(f' (-) IR (11%): ------------ R$ {ir:>8.2f}')
print(f' (-) INSS (8%) ------------ R$ {inss:>8.2f}')
print(f' (-) Sindicato (5% -------- R$ {sindicato:>8.2f}')
print(f' (=) Salário Líquido ------ R$ {salario_liquido:>8.2f}')

