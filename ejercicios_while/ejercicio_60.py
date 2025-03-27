# 60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
rep = 0
multi = 0
op = 0
num = int(input('Introduce un número para hacer su tabla de multiplicar del 1 al 10: '))
while rep < 10:
    rep += 1
    multi += 1
    op = num * multi
    print(op)
print('fin del programa')