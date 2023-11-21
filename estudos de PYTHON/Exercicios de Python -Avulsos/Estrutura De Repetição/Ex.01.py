""" Ex.01 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido."""
while True:
    entrada = input('Digite uma nota entre 0 e 10: ')
    if entrada.isdigit():
        nota = int(entrada)
        if nota not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print('Nota inválida.')
        else:
            print(nota)
            break
