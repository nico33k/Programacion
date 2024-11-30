#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra
secret_w = input('Introduzca por teclado la palabra secreta: ')
for x in range(len(secret_w)):
    let = input('Introduce una letra: ')
    if let in secret_w:
        print('La letra existe')
    else:
        print('La letra no existe')