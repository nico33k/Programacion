# solucion ej 2:
lista1=[]
frase2=''

frase = input('...')

lista1 = frase.split()

palabra = input('Inmtroduce la palabra...: ')

contar=lista1.count(palabra)

frase2=','.join(lista1)
print(contar)
print(frase2)