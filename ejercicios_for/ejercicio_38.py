#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
number = int(input('Introduce el número de notas que deseas introducir: '))

for x in range (0, number):
    nota = float(input('Introduce la nota: '))
    if nota>10 or nota<0:
        print('Has introducido una nota equivocada')
    if nota>=5 and nota<=10:
        print('Has aprobado')
    if nota<5 and nota>=0:
        print('Has suspendido')
