"""Ex. 96 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def calcula_area(largura, comprimento):
    area = largura * comprimento
    print(f"\nA Área para essas Dimensões {largura} X {comprimento} é de {area} m²")


print("-=" * 14)
print("Dimensões do Terreno")
print("-=" * 14)
larg = float(input("Digite a Largura em (m): "))
comp = float(input("Digite a Largura em (m): "))


calcula_area(larg, comp)
