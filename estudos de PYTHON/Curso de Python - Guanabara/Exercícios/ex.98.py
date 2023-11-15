"""Ex. 98 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
    Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p = p * -1

    if p == 0:
        print(
            "[ERRO] Como não o passo não pode ser 0, iremos padronizar como sendo o valor 1."
        )
        p = 1

    if i < f:
        print("-=" * 20)
        print(f"Contagem de {i} até {f} pulando de {p} em {p}")
        sleep(2)
        cont = i
        while cont <= f:
            print(f"{cont} ", end="")
            sleep(0.5)
            cont += p
        print("Fim")
    else:
        cont = i
        print("-=" * 20)
        print(f"Contagem de {i} até {f} pulando de {p} em {p}")
        sleep(2)
        while cont >= f:
            print(f"{cont} ", end="")
            sleep(0.5)
            cont -= p
        print("Fim")
        print("-=" * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez... Escolha um início um fim e um passo.")
ini = int(input("Escolha o início:   "))
fim = int(input("Escolha o fim:      "))
pas = int(input("Escolha o passo:    "))
contador(ini, fim, pas)

while True:
    sair = str(input("Deseja SAIR? [S/N] ")).strip().upper()[0]

    while sair not in ["S", "N"]:
        print("[ERRO] Digite S para SAIR ou N para CONTINUAR")
        sair = str(input("Deseja SAIR? [S/N] ")).strip().upper()[0]

    if sair == "S":
        break
    else:
        ini = int(input("Escolha o início:   "))
        fim = int(input("Escolha o fim:      "))
        pas = int(input("Escolha o passo:    "))
        contador(ini, fim, pas)
print("Encerrando...")
sleep(2)
print("Programa Encerrado!")
