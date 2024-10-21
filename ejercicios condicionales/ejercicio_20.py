#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir pot teclado nÃºmeros entr 0 y 10
var1 = int(input('Introduce un valor entre 0 y 10: '))
var2 = int(input('Introduce otro valor entre 0 y 10 (puede ser el mismo): '))

if var1>10 or var1<0 or var2>10 or var2<0:
    print ('Uno o los dos numeros estan fuera de los l’mites establecidos')
elif var1>var2:
    print('El primer valor:',var1,'es mayor que el segundo valor:',var2)
elif var1<var2:
    print ('El segundo valor:',var2,'es mayor que el primer valor:',var1)
else:
    print ('El primer valor:',var1,'es igual que el segundo valor',var2)