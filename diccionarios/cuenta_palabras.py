archivo = input('Ingresar nombre de Archivo: ')
try:
    manejador = open(archivo)
except:
    print('No se puede abrir el archivo')
    exit()
diccionario_inicial = {}
contador = 0
for linea in manejador:
    linea_lista = linea.split()
    for palabra in linea_lista:
        diccionario_inicial[palabra] = diccionario_inicial.get(palabra, 0) + 1
        

print(diccionario_inicial)
