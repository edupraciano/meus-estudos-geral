""" Ex.03 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
else:
    print('Sexo Inválido')
