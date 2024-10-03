#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso = int(input('Su peso en kilos es: '))
altura = float(input('Su altura en metros es: '))
IMC = peso/altura**2
if IMC>=25:
    print ('Si pesas',peso,'y mides',altura,'tu IMC es:',round (IMC,2),'. Hay sobrepeso')
else:
    print ('Si pesas',peso,'y mides',altura,'tu IMC es:',round (IMC,2),'. No hay sobrepeso')

