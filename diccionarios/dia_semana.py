#archivo = input('Ingresar nombre de Archivo: ')

manejador = open('mbox-short.txt')
diccionario = {}

for linea in manejador:
    if not linea.startswith('From '): continue
    linea = linea.split()
    if linea[2] is not diccionario:
        diccionario[linea[2]] = diccionario.get(linea[2], 0) + 1
print(diccionario)        