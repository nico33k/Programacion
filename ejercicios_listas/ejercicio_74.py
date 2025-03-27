# 
lista1 = ['casa', 'mesa', 'sal', 'sol', 'agua']
lista2 = ['casa', 'luz', 'tres', 'tren', 'sol', 'pan']

rep = [] 
norep = [] 

for x in lista1:
    if x in lista2:
        rep.append(x)
    else:
        norep.append(x)

for x in lista2:
    if x not in lista1 and x not in norep:
        norep.append(x)

print('Están repetidas:', rep)
print('No están repetidas:', norep)