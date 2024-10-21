#19. Programa que introduza 2 números y devuelva cuál de los 2 es mayor, menor o son iguales
var1 = int(input('Introduce el primer valor: '))
var2 = int(input('Introduce el segundo valr: '))

if var1>var2:
    print ('El primer valor:',var1,'es mayor que el segundo valor:',var2)
elif var1<var2:
    print ('El segundo valor:',var2,'es mayor que el primer valor:',var1)
else:
    print ('El primer valor:',var1,'es igual que el segundo valor',var2)