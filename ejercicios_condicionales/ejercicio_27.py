#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un n√∫mero, aparezca un aviso por pantalla
var=input('Introduzca un valor por pantalla: ')

if var.islower()==True:
    print ('Ha introducido una letra en min√scula')
    
elif var.isupper()==True:
    print('Ha introducido una letra en may√∫scula')    
    
elif var.isnumeric()==True:
    print('Ha introducido un número')
    
else:
    print('La letra es mayuscula¿?')