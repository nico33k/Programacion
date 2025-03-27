import math
PI = math.pi
diametro = int(input('El diámetro del círculo es: '))
radio = diametro/2
area = PI*radio**2
perimetro = 2*PI*radio
print ('El área del círculo es:',round (area,1))
print (f'El perímetro del circulo es:{round (perimetro,1)}')
