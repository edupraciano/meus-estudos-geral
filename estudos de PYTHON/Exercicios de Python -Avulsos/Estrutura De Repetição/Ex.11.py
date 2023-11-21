# Ex.11 Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
soma = 0
for c in range(num1, num2 + 1):
    print(f' > {c}', end='')
    soma += c
print()
print(f'A soma dos números é: {soma}.')


