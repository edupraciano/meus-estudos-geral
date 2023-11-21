""" Ex.45 Desenvolver um programa para verificar a nota do aluno em uma prova com 04 questões, o programa deve
perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de
acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma
pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a) Maior e Menor Acerto;
b) Total de Alunos que utilizaram o sistema;
c) A Média das Notas da Turma.

Gabarito da Prova:

Q_01 - A
Q_02 - B
Q_03 - C
Q_04 - D
Q_05 - E
Q_06 - E
Q_07 - D
Q_08 - C
Q_09 - B
Q_10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
alunos usarem o programa.
"""

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
cont = 0
alunos = []
maior_acerto = 0
menor_acerto = 10
alunos_maior = []
alunos_menor = []
total_acertos = 0

"""# Permitindo ao professor digitar o gabarito
print("Digite o gabarito da prova:")
gabarito = [input(f"Resposta da questão {i + 1}: ").strip().upper()[0] for i in range(10)]"""

while True:
    acerto = 0
    aluno = str(input(f'Entre com o nome do {cont + 1}º aluno: ')).upper().strip()
    alunos.append(aluno)

    for i in range(10):
        questao = str(input(f'Digite a resposta da {i + 1}ª questão: ')).strip().upper()[0]
        if questao == gabarito[i]:
            acerto += 1

    total_acertos += acerto

    if acerto > maior_acerto:
        maior_acerto = acerto
        alunos_maior = [aluno]
    elif acerto == maior_acerto:
        alunos_maior.append(aluno)

    if acerto < menor_acerto:
        menor_acerto = acerto
        alunos_menor = [aluno]
    elif acerto == menor_acerto:
        alunos_menor.append(aluno)

    print(f'O aluno {aluno} acertou {acerto} {"questão" if acerto == 1 else "questões"}. Seu número de acertos é: {acerto}')

    cont += 1

    while True:
        sair = str(input('Deseja SAIR? [S/N]: ')).strip().upper()[0]

        if sair in 'SN':
            break
        else:
            print('Entrada Inválida. Digite S para SAIR ou N para continuar.')
            print()

    if sair == 'S':
        break

media = total_acertos / cont

# Formatar a mensagem sobre o MAIOR e MENOR acerto
mensagem_maior_acerto = f'Os alunos com o MAIOR acerto foram {alunos_maior} com {maior_acerto} {"acerto" if maior_acerto == 1 else "acertos"}.'
mensagem_menor_acerto = f'Os alunos com o MENOR acerto foram {alunos_menor} com {menor_acerto} {"acerto" if menor_acerto == 1 else "acertos"}.'

print(mensagem_maior_acerto)
print(mensagem_menor_acerto)
print('-=' * 30)
print(f'Ao todo {cont} {"Aluno" if cont == 1 else "alunos"} {"usou" if cont == 1 else "usaram"} o sistema.')
print(f'São eles: {alunos}')
print(f'A média é de {media:.2f}')
print('Programa Encerrado!')
