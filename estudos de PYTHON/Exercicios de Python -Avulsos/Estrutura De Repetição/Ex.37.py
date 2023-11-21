""" Ex.37 Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia
seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no
campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes."""
mais_alto = mais_baixo = mais_gordo = mais_magro = 0
cod_mais_alto = cod_mais_baixo = cod_mais_gordo = cod_mais_magro = 0
cont = soma_peso = soma_altura = 0
while True:
    cod = int(input('Entre com o seu código: '))

    if cod == 0:
        break

    altura = float(input('Qual a sua altura?: '))
    peso = float(input('Qual o se peso?: '))

    cont += 1
    soma_peso += peso
    soma_altura += altura

    if cont == 1:
        mais_alto = mais_baixo = altura
        mais_gordo = mais_magro = peso
        cod_mais_alto = cod_mais_baixo = cod_mais_gordo = cod_mais_magro = cod
    else:
        if peso > mais_gordo:
            mais_gordo = peso
            cod_mais_gordo = cod
        if peso < mais_magro:
            mais_magro = peso
            cod_mais_magro = cod
        if altura > mais_alto:
            mais_alto = altura
            cod_mais_alto = cod
        if altura < mais_baixo:
            mais_baixo = altura
            cod_mais_baixo = cod

print()
media_dos_pesos = soma_peso / cont
print(f'A média dos pesos é de {media_dos_pesos:.2f} kg')
media_altura = soma_altura / cont
print(f'A média das alturas é de {media_altura:.2f} m')
print(f'O Usuário mais alto é o {cod_mais_alto} com {mais_alto:.2f} m')
print(f'O Usuário mais baixo é o {cod_mais_baixo} com {mais_baixo:.2f} m')
print(f'O Usuário mais gordo é o {cod_mais_gordo} com {mais_gordo:.2f} Kg')
print(f'O Usuário mais magro é o {cod_mais_magro} com {mais_magro:.2f} kg')

print('Programa Encerrado!')
