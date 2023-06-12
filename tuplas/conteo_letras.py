import string

archivo = input('Introduce un archivo: ')

with open(archivo, 'r+') as manejador:
    contador = {}
    for linea in manejador:
        # Elimina los espcios en blaco, al comienzo y al final
        linea = linea.rstrip()
        # Transforma los signos de puntuacion en cadenas vacias
        linea = linea.translate(str.maketrans('', '', string.punctuation))
        # Combierte las letras en minusculas 
        linea = linea.lower()
        # Agragamos cada letra al diccionario y si ya se encuentra aumentamos su valor en 1
        for letra in linea:
            if letra == ' ': continue
            if letra not in contador:
                contador[letra] = 1
            else:
                contador[letra] += 1

    l = list()
    for llave, valor in contador.items():
        l.append((valor, llave))
    l.sort(reverse=True)

for catidad, letra in l[:10]:
    print(letra, catidad)

