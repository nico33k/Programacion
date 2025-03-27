#3
lado = int(input('Introduce el valor de una lado del triángulo: '))

import math
SQRT = math.sqrt
#importo la raíz cuadrada

area = SQRT(3)/4*lado**2
#hago las operaciones para conseguir el área

print ('El área del triángulo es:',round (area,2))
#printeo el resultado
