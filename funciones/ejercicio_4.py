def calculo_de_salario(a, b):
    salario = a * b
    return salario

try:
    horas = float(input('Introdusca las horas: '))
    tarifa = float(input('Introdusca la tarifa por hora: '))
    if horas > 40:
        horas_extras = horas - 40
        horas_normales = 40
        recargo = tarifa * 1.5
        pago = calculo_de_salario(horas_extras, recargo) + calculo_de_salario(horas_normales, tarifa)
        print('Tu pago es: ', pago) 
    else:
        pago = calculo_de_salario(horas, tarifa)
        print('Tu pago es: ', pago)

except:
    print('Por favor, introdusca un numero') 

