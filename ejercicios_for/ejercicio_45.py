#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
vocals = 'aáeéiíoóuú'
vocals_f = ''
consonants_f = ''
word = input('Introduce una palabra: ')

for x in word:
    if x in vocals:
        vocals_f = vocals_f + x
    else:
        consonants_f = consonants_f + x
        
print('Las vocales en la palabra', word, 'son:', vocals_f)
print('Las consonantes en la palabra', word,'son:', consonants_f)