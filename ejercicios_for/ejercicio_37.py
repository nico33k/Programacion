#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido
number = int(input('Introduce el número de notas que deseas introducir: '))

for x in range (0, number):
    nota = float(input('Introduce la nota: '))
    if nota>=5:
        print('Has aprobado')
    else:
        print('Has suspendido')