""" Ex.11 Uma empresa resolveu dar um aumento de salário os seus colaboradores e lhe contrataram para
    desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário atual e baseado
    nos critérios a seguir, responda o que se pede:
    - Salários até R$ 280,00 (incluindo) : aumento de 20%
    - Salários entre R$ 280,00 e R$ 700,00: aumento de 15%
    - Salários entre R$ 700,00 e R$ 1.500,00: aumento de 10%
    - Salários de R$ 1.500,00 em diante: aumento de 5%.
 Após o aumento ser realizado informe na tela:
 a) O salário antes do aumento;
 b) O percentual de aumento aplicado;
 c) O valor do aumento;
 d) O novo salário após o aumento.
"""
salario_atual = float(input('Qual é o salário atual do funcionário? R$ '))
if salario_atual <= 280:
    percentual = 0.20
    reajuste = salario_atual * percentual
    novo_salario = salario_atual + reajuste
    print('-=' * 40)
    print(f'a) O salário antes do aumento : R$ {salario_atual:.2f}. ')
    print(f'b) O percentual de aumento aplicado : {percentual * 100}%. ')
    print(f'c) O valor do aumento : R$ {reajuste:.2f}. ')
    print(f'd) O novo salário após o aumento : R$ {novo_salario:.2f}. ')
    print('-=' * 40)
elif 700 >= salario_atual > 280:
    percentual = 0.15
    reajuste = salario_atual * percentual
    novo_salario = salario_atual + reajuste
    print('-=' * 40)
    print(f'a) O salário antes do aumento : R$ {salario_atual:.2f}. ')
    print(f'b) O percentual de aumento aplicado : {percentual * 100}%. ')
    print(f'c) O valor do aumento : R$ {reajuste:.2f}. ')
    print(f'd) O novo salário após o aumento : R$ {novo_salario:.2f}. ')
    print('-=' * 40)
elif 1500 >= salario_atual > 700:
    percentual = 0.10
    reajuste = salario_atual * percentual
    novo_salario = salario_atual + reajuste
    print('-=' * 40)
    print(f'a) O salário antes do aumento : R$ {salario_atual:.2f}. ')
    print(f'b) O percentual de aumento aplicado : {percentual * 100}%. ')
    print(f'c) O valor do aumento : R$ {reajuste:.2f}. ')
    print(f'd) O novo salário após o aumento : R$ {novo_salario:.2f}. ')
    print('-=' * 40)
else:
    percentual = 0.05
    reajuste = salario_atual * percentual
    novo_salario = salario_atual + reajuste
    print('-=' * 40)
    print(f'a) O salário antes do aumento : R$ {salario_atual:.2f}. ')
    print(f'b) O percentual de aumento aplicado : {percentual * 100}%. ')
    print(f'c) O valor do aumento : R$ {reajuste:.2f}. ')
    print(f'd) O novo salário após o aumento : R$ {novo_salario:.2f}. ')
    print('-=' * 40)
