import socket

url = input('Que pagina quieres leer: ')
host = url.split('/')

try:
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((host[2], 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    misock.send(cmd)

    while True:
        datos = misock.recv(512)
        if len(datos) < 1:
            break
        print(datos.decode(),end='')
    misock.close()

except: print('url incorrecta')