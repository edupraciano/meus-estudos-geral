""" Ex.02 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""
nome = input('Digite o seu nome: ').strip().upper()
while True:
    senha = input('Digite sua senha: ').strip().upper()
    if senha == nome:
        print(f'Esta senha não está dentro dos padrões de segurança, por favor, crie outra senha.')
    else:
        print('Senha criada com sucesso!')
        break
