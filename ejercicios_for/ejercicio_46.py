#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
vocals = 'aáeéiíoóuú'
vocals_f = ''
consonants_f = ''
word = input('Introduce una palabra: ')

for x in word.lower():
    if x in vocals:
        vocals_f = vocals_f + x
    else:
        consonants_f = consonants_f + x
        
print('Las vocales en la palabra', word, 'son:', vocals_f)
print('Las consonantes en la palabra', word,'son:', consonants_f)