archivo = input('Ingresar nombre de Archivo: ')

manejador = open(archivo)
diccionario = {}

for linea in manejador:
    if not linea.startswith('From '): continue
    linea = linea.split()
    if linea[1] is not diccionario:
        diccionario[linea[1]] = diccionario.get(linea[1], 0) + 1

l = list()
for clave, valor in diccionario.items():
    l.append((valor, clave))
l.sort(reverse=True)

print(max(l))