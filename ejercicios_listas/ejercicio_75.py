# 75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados: 
#a. Cantidad total de valores 
#b. Cantidad de números 
#c. Cantidad de letras 
#d. Cantidad de mayúsculas 
#e. Suma de los valores numéricos 
cantnum = 0
cantlet = 0
may = 0
sumatotal = 0
lista1 = ['a','b','D','x','r','X','3','h','w','2','i']

for x in lista1:
    if x.isnumeric():
        cantnum+=1
        sumatotal+=int(x)
    if x.isalpha():
        cantlet+=1
    if x.isupper():
        may+=1
    
numvalores = len(lista1)




print('Número de valores:', numvalores)
print('Cantidad de números:', cantnum)
print('Cantidad de letras:', cantlet)
print('Cantidad de mayúsculas:', may)
print('Suma total de números:', sumatotal)