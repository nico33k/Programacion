# 85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
ans = 's'
import statistics
ingles = []
caste = []
cata = []
while ans == 's':
    input('Introdcue estudiante: ')
    notaing = float(input('Nota ingles: '))
    ingles.append(notaing)
    notacas = float(input('Nota castellano: '))
    caste.append(notacas)
    notacata = float(input('Nota catalán: '))
    cata.append(notacata)
    
    ans = input('¿Desea introducir otro alumno? s/n : ')
    if ans == 'n':
        ingles.sort()
        caste.sort()
        cata.sort()
        print('Ingles: ', ingles)
        print('Castellano: ', caste)
        print('Catalan: ', cata)
        medingles = sum(ingles)
        medcaste = sum(caste)
        medcata = sum(cata)
        print('La media de ingles es: ', medingles/len(ingles))
        print('La media de castellano es: ', medcaste/len(caste))
        print('La media de catalan es: ', medcata/len(cata))
        
        medianingles = statistics.median(ingles)
        mediancaste = statistics.median(caste)
        mediancata = statistics.median(cata)        
        print('La mediana de ingles es: ', medianingles)
        print('La mediana de caste es: ', mediancaste)
        print('La mediana de cata es: ', mediancata)
        break