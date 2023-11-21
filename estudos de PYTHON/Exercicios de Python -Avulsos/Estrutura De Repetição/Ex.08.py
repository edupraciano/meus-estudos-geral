# Ex.08 Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = media = 0
for c in range(5):
    num = float(input(f'Digite o {c + 1}º Número: '))
    soma += num

media = soma / 5
print(f'A soma dos números é: {soma} e a média é {media:.2f}')
