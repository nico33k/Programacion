# 59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos
import random
num = random.randint(1,1000)
num_usuario = 0
rep = 0
while num_usuario != num:
    rep +=1
    num_usuario = int(input('Introduce un número entre 1 y 1000: '))
    if num_usuario<num:
        print('El número introducido es menor')
    elif num_usuario>num:
        print('El número introducido es mayor')
    elif num_usuario == num:
        print('Acertaste, has realizado', rep,' intentos')