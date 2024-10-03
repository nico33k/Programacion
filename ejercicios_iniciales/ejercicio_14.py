#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math 
PI = math.pi
diametro = int(input('El diámetro del círculo es: '))
radio = diametro/2
perimetro = 2*PI*radio
area = PI*radio**2
print ('El perímetro del círculo es: ',round (perimetro,1))
print ('El área del círculo es:',round (area,1))
