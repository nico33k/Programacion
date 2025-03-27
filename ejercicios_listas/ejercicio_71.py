# 71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
lista1 = []
lista2 = []
question = 's'
while not question == 'n':
    question = input('¿Desea intoducir una letra? s/n: ')
    if question == 's':
        letra = input('Introduce una letra: ')
        while letra.isnumeric():
            letra = input('Introduce una letra: ')
        lista1.append(letra)
        lista2=set(lista1)
        
print(lista2)