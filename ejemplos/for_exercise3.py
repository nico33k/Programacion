<<<<<<< HEAD
var='b1enos d23s'
contnum=0
contletra=0

for contador in range (0, len(var)):
    if var[contador].isnumeric():
        contnum+=1
    if var[contador].isalpha():
        contletra+=1
print('El total de letras es:',contletra)
=======
var='b1enos d23s'
contnum=0
contletra=0

for contador in range (0, len(var)):
    if var[contador].isnumeric():
        contnum+=1
    if var[contador].isalpha():
        contletra+=1
print('El total de letras es:',contletra)
>>>>>>> bead4448523cbf34935ece1f39dc81ce20c1e06e
print('El total de números es:',contnum)