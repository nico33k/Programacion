#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0
amount = int(input('Introduzca la cantidad de números que desea introducir: '))
positive = 0
negative = 0
zero = 0
for x in range (0, amount):
    number = float(input('Introduzca un número: '))
    if number>0:
        positive+=1
    if number==0:
        zero+=1
    if number<0:
        negative+=1
print('La cantidad de números positivos es: ',positive)
print('La cantidad de números ceros es: ', zero)
print('La cantidad de números negativos es: ', negative)