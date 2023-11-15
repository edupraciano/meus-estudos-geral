"""
Ex. 93 Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
dados = {}
dados["jogador"] = str(input("Qual o nome do jogador? "))
dados["partidas"] = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
dados["gols"] = []
for g in range(0, dados["partidas"]):
    dados["gols"].append(int(input(f"Quantos goal ele fez na {g + 1}ª partida? ")))
    dados["Total de Gols"] = sum(dados["gols"])
print()
print("-=" * 30)
print("Primeiro modo de apresentar os dados.")
print(dados)
print()
print("-=" * 30)
print("Segundo modo de apresentar os dados.")
for k, v in dados.items():
    print(f"O campo {k} tem o valor: {v}")
print()
print("-=" * 30)
print("Terceiro modo de apresentar os dados.")
print(
    f'O jogador {dados["jogador"]} jogou {dados["partidas"]} partidas e fez {sum(dados["gols"])} gols'
)
for g in range(dados["partidas"]):
    print(f'Na partida {g + 1} ele fez {dados["gols"][g]} gols')
