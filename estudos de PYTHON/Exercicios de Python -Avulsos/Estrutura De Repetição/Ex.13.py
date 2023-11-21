""" Ex.13 Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
segundo número. Não utilize a função de potência da linguagem."""
base = int(input('Digite a base do número: '))
expoente = int(input('Digite a expoente: '))
res = base ** expoente
print(f'Para o número de base {base} com expoente {expoente}, temos como resultado o número {res}.')