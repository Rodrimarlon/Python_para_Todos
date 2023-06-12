horas = float(input('Introdusca las horas: '))
tarifa = float(input('Introdusca la tarifa por hora: '))

if horas > 40:
    horas_extras = horas - 40
    horas_normales = 40
    recargo = tarifa * 1.5
    pago = (horas_normales * tarifa) + (horas_extras * recargo)
    print('Tu pago es: ', pago) 
else:
    pago = horas * tarifa
    print('Tu pago es: ', pago)

