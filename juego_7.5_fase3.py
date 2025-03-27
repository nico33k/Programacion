import random
alias = input('Introdcue tu alias: ')
print('Bienvenido al juego del 7 y medio,', alias)
acumulado = 0
banca_acumulado = 0
question = 's'
banca = ''
while question == 's': 
    carta = 0
    question = 's'
    acumulado = 0
    banca_acumulado = 0
    print("¡Nueva partida!")


    while question == 's' and acumulado < 7.5:
        carta = random.randint(1, 12)
    
        while carta in [8, 9]:
            carta = random.randint(1, 12)
    
        if carta in [10, 11, 12]:
            valor = 0.5
        else:
            valor = carta
        
        question = input(alias +', ¿Quieres carta? s/n: ')
        while question not in ['s', 'n']:
            question = input('Opción invalida, ¿quieres carta? s/n: ')
            
        if question == 's':
            acumulado += valor
            print(alias +',tu carta es:', carta)
            print('Acumulas:', acumulado)
            
            if acumulado > 7.5:
                print('¡Te has pasado de 7.5',alias,'! Ahora es el turno de la BANCA')
                banca = 's'
                
            elif acumulado == 7.5:
                print('Enhorabuena', alias,', has conseguido 7.5. Ahora es el turno de la BANCA')
                banca = 's'
            
    if question == 'n':
        if acumulado >= 6 and acumulado <= 7:
            print(alias,', has sido un poco conservador. Ahora es el turno de la BANCA')
            banca = 's'
            
            
        elif acumulado < 6:
            print(alias,', quizás tendrías que arriesgar un poco ¿no? Ahora es el turno de la BANCA')
            banca = 's'
            
    while banca == 's' and banca_acumulado < 7.5:
        carta = random.randint(1, 12)
        while carta in [8, 9]:
            carta = random.randint(1, 12)
    
        if carta in [10, 11, 12]:
            valor = 0.5
        else:
            valor = carta
            
        banca_acumulado += valor
            
        input('TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta.')   
        
        print('La banca saca:', carta)
        print('La banca acumula:', banca_acumulado)
        
        if banca_acumulado >= 5.0 and banca_acumulado <= 7.5 and banca_acumulado >= acumulado:
            banca = 'n'

    if banca_acumulado > 7.5 and acumulado > 7.5:
        print('Banca y ',alias,', ¡ambos habéis perdido!')
            
    elif banca_acumulado > 7.5 and acumulado <= 7.5 or banca_acumulado < 7.5 and acumulado <= 7.5 and acumulado > banca_acumulado:
        print('Felicidades ',alias,', ¡has vencido a la BANCA!')
            
    elif banca_acumulado <= 7.5 and banca_acumulado == acumulado:
        print('BANCA y ',alias,', ¡habéis empatado!')
        
    elif acumulado > 7.5 and banca_acumulado <= 7.5 or acumulado < 7.5 and banca_acumulado <= 7.5 and banca_acumulado > acumulado:
        print('Lo siento ',alias,', has perdido. ¡La BANCA gana!')
        
    
            
                



    question = input('¿Quieres jugar otra partida? (s/n): ')
    while question not in ['s', 'n']:
        question = input('Opción invalida, ¿quieres jugar otra partida? s/n: ')
    if question == 'n':
        print('Gracias por jugar. ¡Hasta la próxima!')