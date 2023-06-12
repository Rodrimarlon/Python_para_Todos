def calcula_calificacion(puntuacion):
    if puntuacion < 0.0 or puntuacion > 1.0:
        print('Puntuacion Incorrecta')
    elif puntuacion >= 0.9:
        print('Sobresaliente')
    elif puntuacion >= 0.8:
        print('Notable')
    elif puntuacion >= 0.7:
        print('Bien')
    elif puntuacion >= 0.6:
        print('Suficiente')
    elif puntuacion < 0.6:
        print('Insuficiente')

try:
    puntuacion = float(input('Introdusca Puntuacion: '))
    calcula_calificacion(puntuacion)
except:
    print('Puntuacion Incorrecta')

