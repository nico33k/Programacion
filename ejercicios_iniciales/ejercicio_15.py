#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales
import math
PI = math.pi
radio = int(input('El valor del radio es: '))
altura = int(input('El valor de la altura es: '))
area = 2*PI*radio*(altura+radio)
volumen = PI*radio**2*altura
print ('El área de cilindro es:', round (area,2))
print ('El volumen del cilindro es:', round (volumen,2))
