#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente
#inicializo valores a cada variable
num= '6734'
#obtengo su longitud
long=len(num)
#sumo cada digito a partir del índice de cada posición
suma = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if suma%2 == 0:
 print (f"el valor de {suma} es par")
else:
    print ('El valor de',suma,'es impar')