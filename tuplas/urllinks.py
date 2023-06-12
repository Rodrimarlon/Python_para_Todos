import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')

# Recuperar todas las etiquetas de anclaje

etiquetas = sopa('p')
print(len(etiquetas))



"""Ejercicio 4: Cambia el programa urllinks.py para extraer y contar las
etiquetas de párrafo (p) del documento HTML recuperado y mostrar
el total de párrafos como salida del programa. No muestres el texto de
los párrafos, sólo cuéntalos. Prueba el programa en varias páginas web
pequeñas, y también en otras más grandes."""