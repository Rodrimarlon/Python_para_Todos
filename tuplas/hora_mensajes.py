archivo = input('Ingresar nombre de Archivo: ')

with open(archivo) as manejador:
    diccionario = {}

    for linea in manejador:
        if not linea.startswith('From '): continue
        linea = linea.split()
        hora = linea[5].split(':')
        if hora[0] is not diccionario:
            diccionario[hora[0]] = diccionario.get(hora[0], 0) + 1

    l = list()
    for clave, valor in diccionario.items():
        l.append((clave, valor))
        l.sort()
    
    for c, v in l:
        print(c, v)
