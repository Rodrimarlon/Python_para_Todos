manejador_archivos = open('archivo.txt')

contador = 0
for linea in manejador_archivos:
    if linea.startswith('From:'):
        contador = contador + 1
        print(linea) 
print(contador)