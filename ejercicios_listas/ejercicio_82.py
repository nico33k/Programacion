# 82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra 
lista = ['casa' ,'barco','gato','perro','madera','agua','puente','pantalón']
import random
pos = random.randint(0, 7)
word = lista[pos]

ans = ''
while ans != word:
    ans = input('Introduce la palabra secreta: ')
    if ans == word:
        print('ACERTASTE')
        break
    else:
        print('SIGUE JUGANDO')