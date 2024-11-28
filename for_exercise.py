var = 0
total = 0
var_min=int(input('Introduce el valor mínimo: '))
var_max=int(input('Introduce el valor máximo: '))
for contador in range(var_min, var_max):
    total = total+contador
print (total)