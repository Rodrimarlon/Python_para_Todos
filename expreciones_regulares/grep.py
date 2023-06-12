import re

archivo = input('Ingresa un nombre de archivo: ')
exprecion = input('Ingresa una Exprecion Regular: ')


with open(archivo) as f:
    for linea in f:
        linea.rstrip()    
        
