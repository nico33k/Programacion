#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a = int(input('Introduzca el primer valor: '))
b = int(input('Introduzca el segundo valor: '))
c = int(input('Introduzca el tercer valor: '))

op = (b**2)-(4*a*c)


if op>0:
    x1 = (-b+(math.sqrt(op)))/(2*a)
    x2 = (-b-(math.sqrt(op)))/(2*a)
    print ('El valor de x1 es:',x1)
    print('El valor de x2 es:',x2)
    
else:
    print('La raíz no puede ser un valor negativo')