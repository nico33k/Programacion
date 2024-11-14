#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
txt = 'A quién madruga Dios ayuda'

var = input('Introduzca una palabra: ')

if var in txt:
    print('La palabra esá en la frase y está en el índice',txt.find(var))
else:
    print('La palabra no está en la frase')