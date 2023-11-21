""" Ex.03 Faça um programa que leia e valide as seguintes informações:
a) Nome: maior que 3 caracteres;
b) Idade: entre 0 e 150;
c) Salário: maior que zero;
d) Sexo: 'f' ou 'm';
e) Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    entrada = input('Digite seu nome: ')
    if entrada.isalpha():
        nome = str(entrada)
        if len(nome) > 3:
            print('Nome Validado')
            break
        else:
            print('Nome Inválido. Este nome é muito curto, tente outro nome.')
    else:
        print('Nome Inválido, Use apenas letras.')

while True:
    entrada = input('Digite sua idade: ')
    if entrada.isdigit():
        idade = int(entrada)
        if 0 <= idade <= 150:
            print('Idade válida!')
            break
        else:
            print('Idade INVÁLIDA!')
    else:
        print('Idade Inválida, Idade deve estar entre 0 e 150')

while True:
    entrada = input('Digite seu Salário R$: ')
    if entrada.isdigit():
        salario = float(entrada)
        if salario > 0:
            print('Salário Válido.')
            break
        else:
            print('Salário Inválido, Salario deve estar ser maior do que ZERO.')

while True:
    entrada = input('Digite o sexo [M/F]').strip().upper()[0]
    if entrada.isalpha():
        sexo = str(entrada)
        if sexo in 'MF':
            print('Sexo Válido')
            break
        else:
            print('Sexo INVÁLIDO. Escolha M - para Masculino ou F - para Feminino')

print('Escolha C - para Casado | S - para Separado  |  V - para Viúvo ou D - para Desquitado')
while True:

    entrada = input('Digite o Estado Civil [S/C/V/D] ').strip().upper()[0]
    if entrada.isalpha():
        sexo = str(entrada)
        if sexo in 'CSVD':
            print('Estado Civil Válido')
            break
        else:
            print('Estado Civil INVÁLIDO. Escolha C - para Casado ou S - para Separado'
                  'V - para Viúvo ou D - para Desquitado ')

print('Todas as entradas foram Validadas com Sucesso!')
