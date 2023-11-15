# Ex.04 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
    entrada = str(input("digite uma letra: ")).strip().upper()[0]
    if entrada.isdigit():
        print(f'\nEsta entrada não corresponde a uma letra, mas sim um número.')
        break
    if entrada in 'AEIOU':
        print(f'\nA letra digitada é uma vogal.')
    else:
        print(f'\nA letra digitada é uma Consoante.')
    break
