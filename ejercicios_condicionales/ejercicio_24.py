#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
peso = float(input('Introduce el peso: '))
altura = float(input('Introduce la altura en metros: '))

IMC = peso/altura**2

print (f'Si pesas {peso} kilos y mides {altura} metros, tu IMC es de:',round (IMC,2))

if IMC>=25:
    print ('Tienes sobrepeso')
else:
    print('Estás dentro de los parámetros normales')