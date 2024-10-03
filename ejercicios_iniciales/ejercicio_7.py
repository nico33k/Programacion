#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
operador1 = int(input("el valo del operador uno es: "))
operador2 = int(input("el valor del segundo operador es: "))
print ("La suma del operador1 y operador2 es: ", operador1 + operador2)
print ("La resta del operador1 y operador2 es: ", operador1 - operador2)
print ("La multiplicación del operador1 y operador2 es: ", operador1 * operador2)
print ("La división del operador1 y operador2 es: ", round(operador1 / operador2,2))
print ("El exponente del operador1 y operador2 es: ", operador1 ** operador2)
print ("La división entera del operador1 y operador2 es: ", operador1 // operador2)
