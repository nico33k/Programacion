#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado = int(input('El valor de lado es: '))
base_menor = int(input('El valor de la base menor es: '))
base_mayor = int(input('El valor de la base mayor es: '))
altura = int(input('El valor de la altura es: '))
perimetro = base_mayor+base_menor+lado+lado
area = (base_menor+base_mayor)/2 *altura
print ('El perímetro es:',perimetro)
print ('El área es:',area)
