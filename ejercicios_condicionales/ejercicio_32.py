#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
txt = 'A quién madruga Dios ayuda'
palabra = input('Introduce una palabra: ')

txt2 = txt.lower()
palabra2 = palabra.lower()
posicion = txt2.find(palabra2)
if palabra2 in txt2:
    print('La palabra está en la frase y está en el índice',posicion)
else:
    print('La palabra no está en la frase')