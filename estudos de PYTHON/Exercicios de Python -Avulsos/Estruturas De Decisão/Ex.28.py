""" Ex.28 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 kg           Acima de 5 kg
File Duplo      R$ 4,90 por kg          R$ 5,80 por kg
Alcatra         R$ 5,90 por kg          R$ 6,80 por kg
Picanha         R$ 6,90 por kg          R$ 7,80 por kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto
e valor a pagar.
"""

print('''
[1] - Filé Duplo 
[2] - Alcatra    
[3] - Picanha''')

# VALIDAR o tipo de carne
while True:
    entrada = input('\nQual o tipo de carne você vai comprar?:  ')
    if entrada.isdigit() and entrada in ['1', '2', '3']:
        entrada = int(entrada)
        break
    print('[ERRO] Opção inválida. escolha entre as opções: [1, 2 ou 3]')

# VALIDAR a quantidade
while True:
    peso = input(f'Quantos kilos você irá comprar?:  ')
    if peso.replace('.', '', 1).isdigit():
        peso = float(peso)
        break
    else:
        print(f'[ERRO] Digite quanto kilos você irá comprar ')

if entrada == 1 and peso <= 5:
    tipo = 'Filé Duplo'
    preço = 4.9
    valor_sem_desconto = preço * peso
elif entrada == 1 and peso > 5:
    tipo = 'Filé Duplo'
    preço = 5.8
    valor_sem_desconto = preço * peso
elif entrada == 2 and peso <= 5:
    tipo = 'Alcatra'
    preço = 5.9
    valor_sem_desconto = preço * peso
elif entrada == 2 and peso > 5:
    tipo = 'Alcatra'
    preço = 6.8
    valor_sem_desconto = preço * peso
elif entrada == 3 and peso <= 5:
    tipo = 'Picanha'
    preço = 6.9
    valor_sem_desconto = preço * peso
elif entrada == 3 and peso > 5:
    tipo = 'Picanha'
    preço = 7.8
    valor_sem_desconto = preço * peso

# VERIFICAR se a compra será feita no cartão
while True:
    cartão = str(input('A compra será paga usando o Cartão da Loja? [S/N]: ')).strip().upper()[0]
    if cartão in 'SN':
        break
    else:
        print(f'[ERRO] Responda S para SIM e N para não. ')

# Cupom Fiscal
if cartão == 'S':
    desconto = valor_sem_desconto * 0.05
    valor_com_desconto = valor_sem_desconto - desconto
else:
    desconto = 0
    valor_com_desconto = valor_sem_desconto

print()
print('-=' * 20)
print(f'{"Cupom Fiscal":^40}')
print('-=' * 20)
print(f'Tipo de carne: ................ {tipo}')
print(f'Preço total: ................. R$ {valor_sem_desconto:.2f}')
print(f'Tipo de pagamento: .... {"Cartão Tabajara" if cartão == "S" else "Outro"}')
print(f'Valor do desconto: ............ R$ {desconto:.2f}')
print(f'Valor a pagar: ............... R$ {valor_com_desconto:.2f}')
print('Volte Sempre\n')
print('-=' * 20)
print('Programa encerrado')
