

import random

puntuacion = []
lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']
media = 0
sn = 's'
while sn == 's':
    pos = random.randint(0, 7)
    word = lista[pos]
    puntos = 8
    ans = ''  

    while ans != word:
        ans = input('Introduce la palabra secreta: ')
        if ans == word:
            print('¡ACERTASTE!')
            puntuacion.append(puntos)
        else:
            print('SIGUE JUGANDO')
            puntos -= 1

    sn = input('¿Quieres hacer otra partida? (s/n): ')
    
for x in range(len(puntuacion)):
    media += 8
    
print('Puntuaciones por partida:', puntuacion)
print('Tu puntuación total ha sido:', sum(puntuacion))
print('La media de las partidas realizadas es: ', media/2)
if sum(puntuacion)>media/2:
    print('Tienes buena suerte')
else:
    print('Dedícate al parchís')