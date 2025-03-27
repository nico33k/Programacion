# 69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
lista = []
num = int(input('Introduce el número de número que deseas introducir: '))

for x in range(num):
    orden = int(input('Introudce un numero: '))
    lista.append(orden)
lista.sort()
print(lista)