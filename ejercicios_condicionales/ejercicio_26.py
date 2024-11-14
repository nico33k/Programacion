#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
var=input('Introduzca una letra por pantalla: ')

if var.islower()==True:
    print ('La letra es minúscula')
    
elif var.isupper()==True:
    print('La letra es mayúscula')
    
else:
    print('La letra es mayúscula¿?')