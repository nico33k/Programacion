# 61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
rep = 0
multi = 0
op = 0
num = int(input('Introduce un número para hacer su tabla de multiplicar del 1 al 10: '))
while op < 40:
    rep += 1
    multi += 1
    op = num * multi
    print(op)
print('Fin del programa')