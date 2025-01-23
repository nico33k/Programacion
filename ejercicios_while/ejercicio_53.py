#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
rep = 0
suma_total = 0
sino = 'si'
while sino == 'si':
    num1 = int(input('Introduce el primer valor: '))
    num2 = int(input('Introduce el segundo valor: '))
    suma = num1+num2
    print('El resultado de la suma es:', suma)
    suma_total += suma
    rep += 1
    sino = input('Desea repetir la operacion, si o no?: ')
else:
    print('Programa finalizado')
    print('la suma total es:', suma_total, 'y el número de repeticiones es:', rep)