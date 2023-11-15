"""Ex. 95 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
"""
jogadores = []

while True:
    jogador = {}
    jogador["nome"] = str(input("Qual o nome do jogador? "))
    jogador["partidas"] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador["gols"] = []
    for p in range(0, jogador["partidas"]):
        jogador["gols"].append(
            int(input(f"Quantos gols ele fez na {p + 1}ª partida? "))
        )
    jogador["total de gols"] = sum(jogador["gols"])
    jogadores.append(jogador)

    sair = ""
    while True:
        sair = str(input("Deseja SAIR? [S/N]")).strip().upper()[0]
        if sair in "SN":
            break
        print("Digite S para SAIR e N para continuar...")

    if sair == "S":
        break
print(jogadores)
print("-=" * 30)
print(f'{"Código":<6} {"Jogador":<25} {"Gols":^6} {"Total":^6}')


for k, v in iter(jogador):
    print(jogador)
print("=" * 50)
