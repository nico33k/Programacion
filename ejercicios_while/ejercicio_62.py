#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

inicio = min(num1, num2)
fin = max(num1, num2)

print('los números pares son')
for x in range(inicio, fin + 1):
    if x % 2 == 0:
        print(x, end='-')

print('\nlos números impares son')
for x in range(inicio, fin + 1):
    if x % 2 != 0:
        print(x, end='-')