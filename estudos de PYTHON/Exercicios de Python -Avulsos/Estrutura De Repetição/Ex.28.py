""" Ex.28 Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor pago em cada um."""
total_investido = 0
qtde_Cds = int(input('Qual a quantidade total de CDs que você possui? '))
for i in range(qtde_Cds):
    preco_Cd = float(input(f'Quanto custou o {i + 1}º CD? '))
    total_investido += preco_Cd

media = total_investido / qtde_Cds

print(f'\nPara a aquisição de {qtde_Cds} Cds, você precisou investir R$ {total_investido:.2f} e em média os Cds custaram'
      f' R$ {media:.2f}.')
