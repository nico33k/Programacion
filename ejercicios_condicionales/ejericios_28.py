#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
var=input('Introduzca un valor por pantalla: ')

if var.islower()==True:
    print ('Ha introducido una letra en minúscula')
    
elif var.isupper()==True:
    print('Ha introducido una letra en mayúscula')    
    
elif var.isnumeric()==True:
    print('Ha introducido un número')
    
else:
    print('Ha introducido un símbolo')
