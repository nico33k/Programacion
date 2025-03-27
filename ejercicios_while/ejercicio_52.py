# 52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
sino = 'si'
while sino == 'si':
    num1 = int(input('Introduce el primer valor: '))
    num2 = int(input('Introduce el segundo valor: '))
    print('El resultado de la suma es:', num1 + num2)
    sino = input('Desea repetir la operacion, si o no?: ')
else:
    print('Programa finalizado')