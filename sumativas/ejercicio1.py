#1
pos=0
lista=[]
suma=0
num = input('Introduce 6 números separados por un guion: ')
for x in num:
    lista.append(x)
lista.remove('-')
lista.remove('-')
lista.remove('-')
lista.remove('-')
lista.remove('-')
print(lista)

print(max(lista))
print(min(lista))

suma = int(lista[0])+int(lista[1])+int(lista[2])+int(lista[3])+int(lista[4])+int(lista[5])
print(suma/int(len(lista)))

