#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
first = int(input('Introduce el primer intervalo: '))
second = int(input('Introduce el segundo intervalo: '))
if first<second:
    for x in range(first, second):
        print(x, end = '-')
    print(second)
else:
    for x in range(first, second, -1):
        print(x, end = '-')
    print(second)