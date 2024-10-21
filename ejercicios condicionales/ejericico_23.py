#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota = float(input('Introduza una nota entre 0 y 10: '))
if nota<0 or nota>10:
    print ('La nota que has introducido no está entre 0 y 10')
elif nota>=8.5:
    print ('Has sacado un',nota,', por lo que tienes un excelente')
elif nota>=6.5 and nota<8.5:
    print ('Has sacado un',nota,', por lo que tienes un notables')
elif nota>=5 and nota<6.5:
    print ('Has sacado un',nota,', por lo que tienes un bien')
else:
    print ('Has sacado un',nota,', por lo que tienes un insuficiente')