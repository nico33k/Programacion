#40. Crea un programa que cuente todos los números pares hasta el número 50
pares = 0
impares = 0
for x in range(0, 50):
    if x%2==0:
        pares+=1
    else:
        impares+=1
print('El total de pares es: ', pares)
print('El total de impares es: ', impares)