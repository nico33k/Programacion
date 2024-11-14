#Realitzar un programa que permeti introduir una ‘paraula clau’ amb les següents característiques:
print('El password debe tener una longitud de entre 6 y 8 carácteres')
print('La contraseña debe respetar la siguiente secuencia:')
print('Posición 1: un número mayor o igual a 1 y menor o igual a 5')
print('Posición 2: una letra minúscula')
print('Posición 3: una letra mayúscula')
print('Posición 4: uno de los siguientes símbolos *, _, @')
print('Posición 5: una letra minúscula')
print('Posición 6: un número mayor o igual a 6 y menor o igual a 9')
print('Posición 7: un de los siguientes símbolos &, /, #')
print('Posición 8: un número menor o igual a 5')

password = input('Introduzca el password: ')
errores = 0

if len(password)<6 or len(password)>8:
    print('Error, el password tiene una longitud de',len(password),'carácteres y no cumple los requisitos')

elif len(password)==6 or len(password)==7 or len(password)==8:
    if password[0]<str(1) or password[0]>str(5):
        print('Error en el carácter 1', end = ' ')
        errores = errores+1
    
    if password[1].islower() == False:
        print('Error en el carácter 2', end = ' ')
        errores = errores+1
    
    if password[2].isupper() == False:
        print('Error en el carácter 3', end = ' ')
        errores = errores+1

    if not password[3] == '*' and not password[3] == '_' and not password[3] == '@':
        print('Error en el carácter 4', end = ' ')
        errores = errores+1
    
    if password[4].islower() == False:
        print('Error en el carácter 5', end = ' ')
        errores = errores+1
    
    if password[5]<str(6) or password[5]>str(9):
        print('Error en el carácter 6', end = ' ')
        errores = errores+1
        
    if len(password)==7 or len(password)==8:    
        if not password[6] == '&' and not password[6] == '/' and not password[6] == '#':
            print('Error en el carácter 7', end = ' ')
            errores = errores+1
            
    if len(password)==8:
        if password[7]<str(0) or password[7]>str(5):
            print('Error en el carácter 8', end = ' ')
            errores = errores+1
            
    if errores==0:
        print('El formato del PASSWORD es correcto')