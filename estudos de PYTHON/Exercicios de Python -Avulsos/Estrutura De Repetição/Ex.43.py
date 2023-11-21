""" Ex.43 O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
ser encerrado."""
total = 0
while True:
    cod = int(input('Digite o código para o seu pedido: '))
    qtde = int(input(f'Digite a quantidade: '))
    if cod == 100:
        item = 'Cachorro Quente'
        preço = 1.2
    elif cod == 101:
        item = 'Bauru Simples'
        preço = 1.3
    elif cod == 102:
        item = 'Bauru com ovo'
        preço = 1.5
    elif cod == 103:
        item = 'Hambúrguer'
        preço = 1.2
    elif cod == 104:
        item = 'Cheeseburguer'
        preço = 1.3
    elif cod == 105:
        item = 'Refrigerante'
        preço = 1

    valor = preço * qtde
    total += valor

    print(f'O valor a ser pago pelo {item} é de R$ {valor:.2f}\n')

    sair = str(input('Deseja SAIR? [S/N]?: ')).strip().upper()[0]
    if sair == 'S':
        break

print(f'\nO valor total pago foi de R$ {total:.2f}')
print('Obrigado e volte Sempre!')
