import urllib.request, urllib.parse, urllib.error, operator

try:
    url = 'https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt'
    
    manejador = urllib.request.urlopen(url)
    lista = []
    contador = 0
    for linea in manejador:
        linea = linea.decode().split()
        for e in linea:
            lista.extend(e)
    contador = 0
    if contador < 3001:
        for i in lista:
            print(i)
    print(len(lista))        

except Exception as err: print('Error:', err)
    
    
"""Ejercicio 3: Utiliza urllib para rehacer el ejercicio anterior de modo que
(1) reciba el documento de una URL, (2) muestre hasta 3000 caracteres,
y (3) cuente la cantidad total de caracteres en el documento. No te
preocupes de las cabeceras en este ejercicio, simplemente muesta los
primeros 3000 caracteres del contenido del documento."""