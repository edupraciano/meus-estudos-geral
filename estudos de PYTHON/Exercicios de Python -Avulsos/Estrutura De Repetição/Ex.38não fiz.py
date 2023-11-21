""" Ex.38 Um funcionário de uma empresa recebe aumento salarial anualmente: sabe-se que:
a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual (ano atual) desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário."""

salario_inicial = 1000
aumento = 0.015
ano_inicial = 1995
ano_atual = 2023
salario_atual = 0
for ano in range(ano_inicial + 1, ano_atual + 1):
    if ano == 1996:
        salario_atual += salario_inicial * aumento
    else:
        salario_atual += salario_inicial =