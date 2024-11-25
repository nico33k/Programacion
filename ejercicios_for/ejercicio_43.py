#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
word = input('Introduzca una palabra: ')
cont = 0
for x in word:
    print('En la posición', cont,'está la', x)
    cont+=1
    