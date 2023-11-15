"""
Ex.97 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex: escreva (‘Olá, Mundo!’)
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""


def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print(f"  {msg}")
    print("~" * tamanho)


msg = str(input("Digite uma mensagem "))

escreva(msg)
