#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
num = random.randint(1,5)
num_usuario = 0
while num_usuario != num:
    num_usuario = int(input('Introduce un número entre 1 y 5: '))
    if num_usuario != num and num_usuario<6 and num_usuario>0:
        print('Número no acertado')
    elif num_usuario<1 or num_usuario>5:
        print('El número no está entre los valores introducidos')
    elif num_usuario == num:
        print('Número acertado')
    
    