#solucion ej 1:
lista=[]
lista2=[]
lista3=[]

num = input('Introduce 6 números separados por un guion: ')

lista = num.split('-')
print(lista)

for x in lista:
    lista2.append(int(x))
    
maxim = max(lista2)
minim = min(lista2)
promedio=(sum(lista2)/len(lista2))

for x in lista2:
    if x > promedio:
        lista3.append(x)
        
print(maxim)
print(minim)
print(promedio)
print(lista3)