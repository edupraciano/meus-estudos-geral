""" Ex.05 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""

while True:
    while True:
        entrada = input('Entre com a população inicial do País A: ')
        if entrada.isdigit() and int(entrada) > 0:
            populacao_A = int(entrada)
            break
        else:
            print('Entrada Inválida! Digite Apenas Números Positivos.')

    while True:
        entrada = input('Entre com a Taxa de Crescimento do País A: ')
        try:
            taxa_crescimento_A = float(entrada) / 100
            if 0 <= taxa_crescimento_A <= 1:
                break
            else:
                print('Entrada Inválida! A taxa de crescimento deve ser um número entre 0 e 100.')
        except ValueError:
            print('Entrada Inválida! Digite Apenas Números Positivos.')

    while True:
        entrada = input('Entre com a população inicial do País B: ')
        if entrada.isdigit() and int(entrada) > 0:
            populacao_B = int(entrada)
            break
        else:
            print('Entrada Inválida! Digite Apenas Números Positivos.')

    while True:
        entrada = input('Entre com a Taxa de Crescimento do País B: ')
        try:
            taxa_crescimento_B = float(entrada) / 100
            if 0 <= taxa_crescimento_B <= 1:
                break
            else:
                print('Entrada Inválida! A taxa de crescimento deve ser um número entre 0 e 100.')
        except ValueError:
            print('Entrada Inválida! Digite Apenas Números Positivos.')

    if populacao_A <= populacao_B:
        anos = 0
        while populacao_A < populacao_B:
            populacao_A += populacao_A * taxa_crescimento_A
            populacao_B += populacao_B * taxa_crescimento_B
            anos += 1
        print(f'Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.')
    else:
        print('A População do país A precisa ser Menor ou igual a População do país B')

    while True:
        sair = str(input('Deseja SAIR? [S/N]')).strip().upper()[0]
        if sair in "SN":
            break
        else:
            print('Digite S para SAIR e N para continuar!')

    if sair == 'S':
        break
