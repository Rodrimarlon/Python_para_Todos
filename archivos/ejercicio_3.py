archivo = input('Que archivo deseas leer: ')

arch = open(archivo)
contador = 0
valor = 0
for linea in arch:
    linea = linea.rstrip()
    if linea.startswith('X-DSPAM-Confidence:'):
        contador = contador + 1
        valor = valor + float(linea[20:]) 

promedio = valor/contador
print(contador, promedio)