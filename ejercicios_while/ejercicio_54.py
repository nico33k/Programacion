# 54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
rep = 0
suma_total = 0

while suma_total<=50:
    num1 = int(input('Introduce el primer valor: '))
    num2 = int(input('Introduce el segundo valor: '))
    suma = num1+num2
    print('El resultado de la suma es:', suma)
    suma_total += suma
    rep += 1
    if rep == 1:
        print('El total acumulado es:', suma_total,'y llevas',rep,' operación realizada')
    else:
        print('El total acumulado es:', suma_total,'y llevas',rep,' operaciónes realizadas')

else:
    print('Programa finalizado')