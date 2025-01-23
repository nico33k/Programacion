# 55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
rep = 0
suma_total = 0

while suma_total<=50 or suma_total%2==0:
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