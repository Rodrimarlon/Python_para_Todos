#tarchivo = input('Ingresar nombre de Archivo: ')

manejador = open('mbox-short.txt')
diccionario = {}

for linea in manejador:
    if not linea.startswith('Author:'): continue
    linea = linea.split()
    for caracter in linea[1]:
        

    #if linea[1] is not diccionario:
     #   diccionario[linea[1]] = diccionario.get(linea[1], 0) + 1
