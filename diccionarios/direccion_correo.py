archivo = input('Ingresar nombre de Archivo: ')

manejador = open(archivo)
diccionario = {}

for linea in manejador:
    if not linea.startswith('Author:'): continue
    linea = linea.split()
    palabra = linea[1]
    arroba = palabra.find('@')
    direccion = palabra[arroba + 1:]
    if direccion is not diccionario:
        diccionario[direccion] = diccionario.get(direccion, 0) + 1

print(diccionario)
