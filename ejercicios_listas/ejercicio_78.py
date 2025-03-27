# 78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir 
lista1 = ['a','b','D','x','r','X','3','h','w','2','i']
ans = 's'
while ans == 's':
    ans = input('Deseas introducir otro valor s/n:')
    if ans == 'n':
        break
    
    delete = input('Introduce el valor que desea eliminar: ')
    
    if not delete.isnumeric():
        print('Introduce un valor numérico')
        
    elif delete.isnumeric() and delete in lista1:
        lista1.remove(delete)
        print(lista1)
        
    elif delete.isnumeric and delete not in lista1:
        print('El valor introducido no está en la lista ')
        
