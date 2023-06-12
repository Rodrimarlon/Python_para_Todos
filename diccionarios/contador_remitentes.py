archivo = input('Ingresar nombre de Archivo: ')

manejador = open(archivo)
diccionario = {}

for linea in manejador:
    if not linea.startswith('Author:'): continue
    linea = linea.split()
    if linea[1] is not diccionario:
        diccionario[linea[1]] = diccionario.get(linea[1], 0) + 1


mayor = max(diccionario, key=diccionario.get)
print(mayor, diccionario[mayor])