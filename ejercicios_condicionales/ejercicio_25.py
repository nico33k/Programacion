#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos
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