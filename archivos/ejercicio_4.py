archivo = input('Ingesa un nombre de archivo: ')
if archivo == 'na na boo boo':
    print('NA NA BOO BOO para ti idiota!!')
try:
    contador = 0
    for linea in archivo:
        contador = contador + 1
    print(f'El archivo tiene {contador} lineas')

except:
    print('No se puede abrir el archivo') 
