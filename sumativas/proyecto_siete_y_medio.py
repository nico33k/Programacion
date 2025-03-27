import random
print('Bienvenido al juego del 7 y medio')
deposito = 100
carta = 0
question = 's'
acumulado = 0
while question == 's' and acumulado < 7.5:
    carta = random.randint(1, 12)
    question = input('¿Quieres carta? s/n: ')
    if question == 's':
        acumulado += carta
        print('Tu carta es:', carta)
        print('Acumulas:', acumulado)
    if acumulado > 7.5:
        print('Has perdido la partida!')
        deposito -= 10
    if acumulado == 7.5:
        print('Enhorabuena, has ganado la partida')
        deposito += 10
if question == 'n':
    if acumulado == 6 or acumulado == 7:
        print('Has sido un poco conservador')
        deposito += 5
    if acumulado < 6:
        print('Quizás tendrías que arriesgar un poco ¿no?')
        deposito -= 5
                