""" Ex.12 Faça umm programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
    que depende do salário bruto (conforme a tabela a baixo) e que o FGTS corresponde a 11% do salário bruto, mas não é
    descontado (é a empresa que deposita).
    O salário líquido corresponde ao salário bruto menos os descontos. O Programa deverá pedir ao usuário o valor da sua
    hora e a quantidade de horas trabalhadas no mês.

 DESCONTO DO IR:
 - Salário Bruto até R$ 900,00 (inclusive): ISENTO
 - Salário Bruto até R$ 1.500,00 (inclusive): Desconto de 5%
 - Salário Bruto até R$ 2.500,00 (inclusive): Desconto de 10%
 - Salário Bruto acima de R$ 2.500,00 (inclusive): Desconto de 20%.
 Imprima na tela as informações conforme o exemplo abaixo:

 No exemplo o valor da hora é 5 e a quantidade de hora é 220.
     Salário bruto: (5 * 220) ...... : R$ 1.100,00
     (-) IR (5%) ................... : R$    55,00
     (-) INSS (10%) ................ : R$   110,00
     (-) FGTS (11%) ................ : R$   121,00
    Total de descontos............. : R$   165,00
    Salário Líquido................ : R$   935,00
"""
qtde_horas = int(input(f'\nQuantas horas foram trabalhadas no mês? '))
valor_hora = int(input(f'Qual o Valor da hora trabalhada? R$ '))
print()
salario_bruto = qtde_horas * valor_hora


if salario_bruto <= 900:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    ir = 0
    total_de_descontos = inss + ir
    salario_liquido = salario_bruto - total_de_descontos
    print('-=' * 35)
    print(f'Para um salário de R$ {salario_bruto:.2f} este é o extrato da folha de pagamento. ')
    print(f'{"Salário Bruto":<20}{"...................... ":<20} R$ {salario_bruto:7.2f} ')
    print(f'{"(-) IR (ISENTO)":<20}{"...................... ":<20} R$ {ir:7.2f} ')
    print(f'{"(-) INSS (10%)":<20}{"...................... ":<20} R$ {inss:7.2f} ')
    print(f'{"(-) FGTS (11%)":<20}{"...................... ":<20} R$ {fgts:7.2f} ')
    print(f'{"Total de Descontos":<20}{"...................... ":<20} R$ {total_de_descontos:7.2f} ')
    print(f'{"Salário Líquido":<20}{"...................... ":<20} R$ {salario_liquido:7.2f} ')
    print('-=' * 35)
elif 900 < salario_bruto <= 1500:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    ir = salario_bruto * 0.05
    total_de_descontos = inss + ir
    salario_liquido = salario_bruto - total_de_descontos
    print('-=' * 35)
    print(f'Para um salário de R$ {salario_bruto:.2f} este é o extrato da folha de pagamento. ')
    print(f'{"Salário Bruto":<20}{"...................... ":<20} R$ {salario_bruto:7.2f} ')
    print(f'{"(-) IR (5%)":<20}{"...................... ":<20} R$ {ir:7.2f} ')
    print(f'{"(-) INSS (10%)":<20}{"...................... ":<20} R$ {inss:7.2f} ')
    print(f'{"(-) FGTS (11%)":<20}{"...................... ":<20} R$ {fgts:7.2f} ')
    print(f'{"Total de Descontos":<20}{"...................... ":<20} R$ {total_de_descontos:7.2f} ')
    print(f'{"Salário Líquido":<20}{"...................... ":<20} R$ {salario_liquido:7.2f} ')
    print('-=' * 35)
elif 1500 < salario_bruto <= 2500:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    ir = salario_bruto * 0.10
    total_de_descontos = inss + ir
    salario_liquido = salario_bruto - total_de_descontos
    print('-=' * 35)
    print(f'Para um salário de R$ {salario_bruto:.2f} este é o extrato da folha de pagamento. ')
    print(f'{"Salário Bruto":<20}{"...................... ":<20} R$ {salario_bruto:7.2f} ')
    print(f'{"(-) IR (10%)":<20}{"...................... ":<20} R$ {ir:7.2f} ')
    print(f'{"(-) INSS (10%)":<20}{"...................... ":<20} R$ {inss:7.2f} ')
    print(f'{"(-) FGTS (11%)":<20}{"...................... ":<20} R$ {fgts:7.2f} ')
    print(f'{"Total de Descontos":<20}{"...................... ":<20} R$ {total_de_descontos:7.2f} ')
    print(f'{"Salário Líquido":<20}{"...................... ":<20} R$ {salario_liquido:7.2f} ')
    print('-=' * 35)
elif salario_bruto > 2500:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    ir = salario_bruto * 0.20
    total_de_descontos = inss + ir
    salario_liquido = salario_bruto - total_de_descontos
    print('-=' * 35)
    print(f'Para um salário de R$ {salario_bruto:.2f} este é o extrato da folha de pagamento. ')
    print(f'{"Salário Bruto":<20}{"...................... ":<20} R$ {salario_bruto:7.2f} ')
    print(f'{"(-) IR (20%)":<20}{"...................... ":<20} R$ {ir:7.2f} ')
    print(f'{"(-) INSS (10%)":<20}{"...................... ":<20} R$ {inss:7.2f} ')
    print(f'{"(-) FGTS (11%)":<20}{"...................... ":<20} R$ {fgts:7.2f} ')
    print(f'{"Total de Descontos":<20}{"...................... ":<20} R$ {total_de_descontos:7.2f} ')
    print(f'{"Salário Líquido":<20}{"...................... ":<20} R$ {salario_liquido:7.2f} ')
    print('-=' * 35)
