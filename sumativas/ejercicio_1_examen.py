#1
var_1 = float(input('Introduce el primer número: '))
#en esta línea el error era que no había un float, por lo que el programa no detectaba la variable como un número, así que he tenido que añadirlo
var_2 = float(input('Intoduce el segundo número: '))
#en esta línea, aparte del float había otro error, las comillas. El texto no estaba entre comillas, así que las he añadido.

var_total = var_1+var_2
#En esta línea había 3 errores, la variable var_total no tenía el guión, y las variables var_1 y var_2 tenían un nombre diferente que antes.

print(f'el resultado de sumar {var_1} y {var_2} es:',var_total)
#En esta línea también había varios errores, f no tenía que ir seguido de una coma, var_1 y var_2 no tenían que ir entre paréntesis, sino entre llaves, y la última variable tenía un nombre diferente y no tenía una coma delante, así que la he llamado var_total (igual que antes), y le he añadido la coma.
