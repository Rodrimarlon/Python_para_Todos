import urllib.request, urllib.parse, urllib.error
import json 
import ssl


clave_api = False

if clave_api is False:
    clave_api = 42
    url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'
else:
    url_de_servicio = 'https://maps.googleapis.com/maps/api/geocode/json?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    direccion = input('Ingresa una ubicación: ')
    if len(direccion) < 1: break

    parms = dict()
    parms['address'] = direccion
    if clave_api is not False: parms['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(parms)

    print('Recuperando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    print('Recuperados', len(datos), 'caracteres')

    try:
        js = json.loads(datos)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        print(datos)
        continue
    
    try:
        codigo_pais = js['results'][0]['address_components'][3]['short_name']
        print(codigo_pais)
        

    except: print('Codigo de pais no Encontrado')




    """Ejercicio 1: Modifica geojson.py o geoxml.py para imprimir en pantalla
el código de país de dos caracteres de los datos recuperados. Añade
comprobación de errores, de modo que tu programa no rastree los datos
si el código del país no está presente. Una vez que lo tengas funcionando,
busca “Océano Atlántico” y asegúrate de que es capaz de gestionar
ubicaciones que no estén dentro de ningún país."""