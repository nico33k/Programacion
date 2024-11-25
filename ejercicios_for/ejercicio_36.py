#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario
num = int(input('Introduzca el número de números naturales que quiere sumar: '))
suma = 0
for contador in range(num+1):
    suma=suma+contador
print('La suma total de números naturales es:', suma)