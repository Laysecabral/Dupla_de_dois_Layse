from random import randint

numero_clientes = 1000
lista_de_respostas = []

while numero_clientes > 0:
    lista_de_respostas.append(randint(1,5))

respostas_1 = lista_de_respostas.count(1)
respostas_2 = lista_de_respostas.count(2)
respostas_3 = lista_de_respostas.count(3)
respostas_4 = lista_de_respostas.count(4)
respostas_5 = lista_de_respostas.count(5)