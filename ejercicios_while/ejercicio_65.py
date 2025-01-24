# 65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
num = 0
num_provi = 0
pares = 0
impares = 0
positive = 0
negative = 0
ceros = 0
suma_total = 0
num_provi = int(input('Introdcue un número: '))
if num_provi == -99
num_may = num_provi
num_men = num_provi
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
        if num>num_may:
            num_may == num
        if num<num_men:
            num_men == num

print('El número de pares es:', pares)
print('El número de impares es', impares)
print('El número de positivos es',positive)
print('El número de negativos es',negative)
print('El número de ceros es',ceros)
print('El total es',suma_total)
print('El número mayor es', num_may)
print('El número menor es', num_men)