# 70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
lista1 = []
lista2 = []

num = int(input('Introdcue el número de palabra que deseas introducir: '))

for x in range(num):
    word = input('Intrdocue una palabra: ')
    lista1.append(word)
    
lista1.sort()
print('La lista 1 contiente:', lista1)

lista2 = lista1
lista2.reverse()
print('La lista 2 contiene:', lista2)