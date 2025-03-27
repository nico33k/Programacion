# 51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While
num = int(input('Introduce el número de veces que se repita la frase buenos días: '))
count = 0
while count<num:
    count+=1
    print('Buenos días')