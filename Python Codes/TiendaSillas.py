def descuento():
    tipo_cliente = input('Eres cliente frecuente o normal? ')
    if tipo_silla == 'basica':
        precio = 700
        precio = (precio*cantidad)
        print(f'Precio: ${precio}')
        if tipo_cliente == 'frecuente':
            descuento = precio*.2
            print(f'Descuento: ${descuento}')
            total = precio - descuento
            print(f'Total: ${total}')
        elif tipo_cliente == 'normal':
            if 10000<=precio<20000:
                descuento = precio*.1
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')
            elif precio>=20000:
                descuento = precio*.15
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')
                
    elif tipo_silla == 'estandar':
        precio = 900
        precio = (precio*cantidad)
        print(f'Precio: ${precio}')
        if tipo_cliente == 'frecuente':
            descuento = precio*.2
            print(f'Descuento: ${descuento}')
            total = precio - descuento
            print(f'Total: ${total}')
        elif tipo_cliente == 'normal':
            if 10000<=precio<20000:
                descuento = precio*.1
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')
            elif precio>=20000:
                descuento = precio*.15
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')


    elif tipo_silla == 'de lujo':
        precio = 1500
        precio = (precio*cantidad)
        print(f'Precio: ${precio}')
        if tipo_cliente == 'frecuente':
            descuento = precio*.2
            print(f'Descuento: ${descuento}')
            total = precio - descuento
            print(f'Total: ${total}')
        elif tipo_cliente == 'normal':
            if 10000<=precio<20000:
                descuento = precio*.1
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')
            elif precio>=20000:
                descuento = precio*.15
                print(f'Descuento: ${descuento}')
                total = precio - descuento
                print(f'Total: ${total}')



tipo_silla = input('Que tipo de silla vas a comprar? (basica, estandar, de lujo) ')
cantidad = int(input('Cuantas quieres? '))

descuento()
