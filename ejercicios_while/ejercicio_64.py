# 64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
num = 0
pares = 0
impares = 0
positive = 0
negative = 0
ceros = 0
suma_total = 0
while num != -99:
    num = int(input('Introduce un número: '))
    if num != -99:
        suma_total += num
        if num%2 == 0:
            pares+=1
        if num%2 == 1:
            impares+=1
        if num>0:
            positive+=1
        if num<0:
            negative+=1
        if num == 0:
            ceros+=1

print('El número de pares es:', pares)
print('El número de impares es', impares)
print('El número de positivos es',positive)
print('El número de negativos es',negative)
print('El número de ceros es',ceros)
print('El total es',suma_total)