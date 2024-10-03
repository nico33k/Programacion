#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
dividendo = float(input('El dividendo es: '))
divisor = float(input('El divisor es: '))
cociente = dividendo/divisor
resto = dividendo%divisor
if dividendo%2==0:
    print ('El cociente es:',cociente)
    print ('El resto es:',resto)
    print ('El dividendo es par')
else:
    print ('El cociente es:',cociente)
    print ('El resto es:',resto)
    print ('El dividendo es impar')
