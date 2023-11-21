""" Ex.15 A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
Faça um programa capaz de gerar a série até o n−ésimo termo."""
n = int(input('Digite o valor de n: '))
if n == 0 or n == 1:
    print(f'O {n}º terno da sequencia de Fibonacci é 1.')
else:
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b
print()
print(f'O {n}º termo da sequencia de Fibonacci é {b} ')

