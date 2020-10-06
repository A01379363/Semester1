#calcula el total de impuestos que debe pagar

renta = float(input('Cual es tu renta anual? '))

if renta<10000:
    print('Tipo de impuesto: 5%')
    print('Debes pagar:', (renta/100)*5)

elif 10000<=renta<20000:
    print('Tipo de impuesto: 15%')
    print('Debes pagar:', (renta/100)*15)

elif 20000<=renta<35000:
    print('Tipo de impuesto: 20%')
    print('Debes pagar:', (renta/100)*20)

elif 35000<=renta<60000:
    print('Tipo de impuesto: 30%')
    print('Debes pagar:', (renta/100)*30)

elif renta>=60000:
    print('Tipo de impuesto: 45%')
    print('Debes pagar:', (renta/100)*45)
    
