"""Ex.19 Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de
organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

[ 1 ] - Windows Server
[ 2 ] - Unix
[ 3 ] - Linux
[ 4 ] - Netware
[ 5 ] - Mac OS
[ 6 ] - Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado
da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma
das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá
calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi
dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
print('\nQual o melhor Sistema Operacional para uso em servidores?')

print("""
[ 1 ] - Windows Server
[ 2 ] - Unix
[ 3 ] - Linux
[ 4 ] - Netware
[ 5 ] - Mac OS
[ 6 ] - Outro""")
print()

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []

while True:
    entrada = input('Qual o seu voto? (Digite 0 para encerrar): ')

    if entrada.isdigit():
        voto = int(entrada)

        if 0 <= voto <= 6:

            if voto == 0:
                break
            if voto == 1:
                lista1.append(voto)
            elif voto == 2:
                lista2.append(voto)
            elif voto == 3:
                lista3.append(voto)
            elif voto == 4:
                lista4.append(voto)
            elif voto == 5:
                lista5.append(voto)
            elif voto == 6:
                lista6.append(voto)

        else:
            print('Entrada Inválida! Digite de 1 a 6.')
    else:
        print('Entrada Inválida! Digite de 1 a 6.')

tamanho_da_lista_geral = len(lista1) + len(lista2) + len(lista3) + len(lista4) + len(lista6) + len(lista6)

print()
print(f'{"Sistema Operacional":<25} {"Votos":^10} {" % ":^10}')
print('-=' * 25)

# para a Lista 01
votos_1 = len(lista1)
percent_lista1 = (votos_1 / tamanho_da_lista_geral) * 100
print(f'{"Windows Server":<25} {votos_1:^10} {percent_lista1:^10.2f}%')

# para a Lista 02
votos_2 = len(lista2)
percent_lista2 = (votos_2 / tamanho_da_lista_geral) * 100
print(f'{"Unix":<25} {votos_2:^10} {percent_lista2:^10.2f}%')

# para a Lista 03
votos_3 = len(lista3)
percent_lista3 = (votos_3 / tamanho_da_lista_geral) * 100
print(f'{"Linux":<25} {votos_3:^10} {percent_lista3:^10.2f}%')

# para a Lista 04
votos_4 = len(lista4)
percent_lista4 = (votos_4 / tamanho_da_lista_geral) * 100
print(f'{"Netware":<25} {votos_4:^10} {percent_lista4:^10.2f}%')

# para a Lista 05
votos_5 = len(lista5)
percent_lista5 = (votos_5 / tamanho_da_lista_geral) * 100
print(f'{"Mac OS":<25} {votos_5:^10} {percent_lista5:^10.2f}%')

# para a Lista 06
votos_6 = len(lista6)
percent_lista6 = (votos_6 / tamanho_da_lista_geral) * 100
print(f'{"Outro":<25} {votos_6:^10} {percent_lista6:^10.2f}%')

print('-=' * 25)
print(f'{"Total":<25} {tamanho_da_lista_geral:^10}')

print()
print('Programa Encerrado')