#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota = float(input('Introduza una nota entre 0 y 10: '))
if nota<0 or nota>10:
    print ('La nota que has introducido no estas entre 0 y 10')
elif nota>=5:
    print ('Has sacado un',nota,', por lo que estas aprobado')
else:
    print ('Has sacado un',nota,', por lo que estas suspendido')