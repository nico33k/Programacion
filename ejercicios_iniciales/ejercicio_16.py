#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
SQRT = math.sqrt
valor = int(input('El valor de la raíz cuadrada es: '))
raiz_cuadrada = SQRT(valor)
division = raiz_cuadrada/2
print ('El resultado de la raíz cuadrada es:',round (raiz_cuadrada,1))
print ('El resultado de la división es:',round (division))
