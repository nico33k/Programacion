# 73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1 = ['casa', 'mesa', 'sal', 'sol', 'agua']
lista2 = ['casa', 'luz', 'tres', 'tren', 'sol', 'pan']

rep = []
norep = []

for x in lista1:
    if x in lista2:
        rep.append(x)
    else:
        norep.append(x)


print('Están repetidas:',rep)        
print('No están repetidas:',norep)
