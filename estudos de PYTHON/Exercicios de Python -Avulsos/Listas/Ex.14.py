"""Ex.14 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
lista_perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
                   "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas_sim = 0

for i in range(5):
    pergunta = str(input(f'{lista_perguntas[i]} (Responda SIM ou NÃO): ')).upper().strip()[0]
    if pergunta == 'S':
        respostas_sim += 1

if respostas_sim == 2:
    classificada = 'Suspeita'
elif respostas_sim == 3 or respostas_sim == 4:
    classificada = 'Cúmplice'
elif respostas_sim == 5:
    classificada = 'Assassino'
else:
    classificada = 'Inocente'

print(f'A pessoa foi considerada como: {classificada}.')
