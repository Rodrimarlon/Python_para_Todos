cantidad_num = []

while True:
    num = input('introduce un numero: ')
    if num == 'fin':
        num = str(num)
        print(int(sum(cantidad_num)), int(len(cantidad_num)), int(max(cantidad_num)), int(min(cantidad_num)))
        break
    try:
        num = float(num)
        float(num)
        cantidad_num.append(num)
    except:
        print('Dato Incorrecto')

print('¡Terminado!')