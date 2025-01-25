# 66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 
import random
import time
t_inicial = time.time()
num = 0
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
while time.time() - t_inicial < 3:
    num =random.randint(1, 6)
    if num == 1:
        uno+=1
    if num == 2:
        dos+=1
    if num == 3:
        tres+=1
    if num == 4:
        cuatro+=1
    if num == 5:
        cinco+=1
    if num == 6:
        seis+=1
print('Uno:',uno)
print('Dos:',dos)
print('Tres:',tres)
print('Cuatro:',cuatro)
print('Cinco:',cinco)
print('Seis:',seis)
