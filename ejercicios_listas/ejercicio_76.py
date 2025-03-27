# 76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
ans = int(input('Introduce 1 para visualizar en orden ascendente o 2 en descendente: '))
num = []
words_low = []
words_up = []
lista1 = ['a','b','D','x','r','X','3','h','w','2','i']
for x in lista1:
    if x.isnumeric():
        num.append(int(x))
    if x.islower():
        words_low.append(x)
    if x.isupper():
        words_up.append(x)

num.sort(reverse=(ans == 2))
words_up.sort(reverse=(ans == 2))
words_low.sort(reverse=(ans == 2))

words=words_low+words_up

print(num)
print(words)