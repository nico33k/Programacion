# 80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
lista1 = []

numero = input('Introduce un número: ')

lista1 = numero.split('.')

if len(lista1) != 2:
    print('no es un decimal')
else:
    if lista1[0].isnumeric() and lista1[1].isnumeric():
        print('es decimal')
    else:
        print('no es un decimal')