# 72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
lista1 = []
lista2 = []
question = 's'
acentos = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù']
while not question == 'n':
    question = input('¿Desea intoducir una letra? s/n: ')
    if question == 's':
        letra = input('Introduce una letra: ')
        while letra.isnumeric():
            letra = input('Introduce una letra: ')
        if letra not in acentos:
            lista1.append(letra)
            lista2=set(lista1)
print(lista2)