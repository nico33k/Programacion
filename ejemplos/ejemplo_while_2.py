import random
num_secret = random.randint(1, 100)
num_usuario = 0
while num_usuario != num_secret:
    num_usuario = int(input('Adivine el número secreto: '))
    if num_usuario != num_secret:
        print('No lo has adivinado')
    if num_usuario == num_secret:
        print('Lo has adivinado, felicidades')
