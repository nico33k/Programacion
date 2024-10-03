#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
menores = int(input('¿Cuántos menores asistirán?: '))
adultos = int(input('¿Cuántos adultos asistirán?: '))
precio_entrada = 12
precio_sin_descuento_menores = menores*precio_entrada
descuento_menores = (50/100)*precio_sin_descuento_menores
precio_final_menores = precio_sin_descuento_menores-descuento_menores

precio_sin_descuento_adultos = adultos*precio_entrada
descuento_adultos = (10/100)*precio_sin_descuento_adultos
precio_final_adultos = precio_sin_descuento_adultos-descuento_adultos

precio_total = precio_final_menores+precio_final_adultos

print ('El precio total para',menores,'menor/es es de:',round (precio_final_menores,2))
print ('El precio total para',adultos,'adulto/s es de:',round (precio_final_adultos,2))
print ('El precio total de',menores,'menor/es y de',adultos,'adulto/s es de:',round (precio_total,2))
