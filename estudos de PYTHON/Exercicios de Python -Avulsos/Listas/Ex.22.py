"""Ex.22 Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção
de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de
200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
- necessita da esfera;
- necessita de limpeza;
- necessita troca do cabo ou conector;
- quebrado ou inutilizado.
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

lista1 = []  # necessita da esfera
lista2 = []  # necessita de limpeza
lista3 = []  # necessita troca do cabo ou conector
lista4 = []  # quebrado ou inutilizado
total = 0

while True:
    identificação = int(input('Entre com o Id do mouse: '))

    if identificação == 0:
        break

    tipo_defeito = int(input('Entre com o tipo de Defeito [1 -4]: '))

    if tipo_defeito == 1:
        lista1.append(tipo_defeito)
    elif tipo_defeito == 2:
        lista2.append(tipo_defeito)
    elif tipo_defeito == 3:
        lista3.append(tipo_defeito)
    elif tipo_defeito == 4:
        lista4.append(tipo_defeito)

    total += 1

print(f'\nQuantidade de mouses: {total}')
print()
print(f'{"Situação":<40} {"Quantidade":<10}      {"Percentual":<200}')
print(f'{"1- necessita da esfera":<40} {len(lista1):^10}      {len(lista1) / total * 100:^6.2f}%')
print(f'{"2- necessita de limpeza":<40} {len(lista2):^10}      {len(lista2) / total * 100:^6.2f}%')
print(f'{"3- necessita troca do cabo ou conector":<40} {len(lista3):^10}      {len(lista3) / total * 100:^6.2f}%')
print(f'{"4- quebrado ou inutilizado":<40} {len(lista4):^10}      {len(lista4) / total * 100:^6.2f}%')
