# 58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
num = random.randint(1,5)
num_usuario = 0
rep = 0
while rep<3 and num_usuario != num:
    rep +=1
    num_usuario = int(input('Introduce un número entre 1 y 5: '))
    if num_usuario != num and num_usuario<6 and num_usuario>0:
        print('Número no acertado')
    elif num_usuario<1 or num_usuario>5:
        print('El número no está entre los valores introducidos')
    elif num_usuario == num:
        print('Número acertado')
    if rep == 3 and num_usuario != num:
        print('Se te han agotado los intentos')