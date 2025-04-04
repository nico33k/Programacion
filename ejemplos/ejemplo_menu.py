#hacer menú (practica para examen)
precio1 = 5
precio2= 6

print('1.Gladiator (5€)')
print('2.Aquaman(6€)')
print('3.Malefica(5€)')

peli = input('Introduce el número de la película que deseas ver: ')

if peli.isnumeric()==True:
    if peli=='1' or peli=='3':
        print('El precio es de', precio1,'€')
    elif peli=='2':
        print('El precio es de',precio2,'€')
    else:
        print('El número introducido no es de ninguna película')
else:
    print('No has introducido un número')
 

