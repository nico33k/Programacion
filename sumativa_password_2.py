# password.2
print('Instrucciones: el password debe ser de ocho carácteres y debe contener: 3 números, entre el 0-5 los tres, 3 letras, dos mayúsculas y una minúscula, y 2 símbolos, @ o & o / o *')
num = 0
letra_may = 0
letra_min = 0
simb = 0
for x in range(0, 3):
    password = input('Introduce el password: ')
    if len(password)!=8:
        print('Error, el password tiene una longitud de', len(password), 'y no cumple los requisistos')
    elif len(password)==8:
        for y in password:
            if y.isnumeric() and int(y) <= 5:
                num +=1
            elif y.isupper():
                letra_may+=1
            elif y.islower():
                letra_min+=1
            elif y in '@&/*':
                simb+=1
        if num!=3:
            print('Error, el password no contiene exactamente 3 números entre 1 y 5')
        if letra_may!=2:
            print('Error, el password no contiene exactamente 2 letras mayúsculas')
        if letra_min!=1:
            print('Error, el password no contiene exactamente 1 letra minúscula')
        if simb!=2:
            print('Error, el password no contiene exactamente 2 de los símbolos & / @ *')
        else:
            print('El password es correcto')