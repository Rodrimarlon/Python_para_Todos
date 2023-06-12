archivo = input('Ingresar nombre de Archivo: ')
manejador = open(archivo)
lista_inicial = []
for linea in manejador:
    linea_lista = linea.split()
    for palabra in linea_lista:
        if palabra in lista_inicial:
            continue
        else:
            lista_inicial.append(palabra)
lista_inicial.sort()
print(lista_inicial)
