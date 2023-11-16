# Ex.07 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
larg = float(input('Digite a largura em metros '))
alt = float(input('Digite a altura em metros '))
area = larg * alt
print(f'A área para essas dimensões é {area}m² e o seu dobro é: {area * 2}m²')
