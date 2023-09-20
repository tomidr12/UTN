'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:

A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:

* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)

B) Luego del ingreso mostrar en pantalla todos los datos.

C) Realizar los siguientes informes:

1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.
'''








nombres = ['Tomas', 'Albana', 'Walter', 'Thiago', 'Dante', 'Owen']
montos = [100, 10, 501, 100000, 510, 1000]
instrumentos = [50, 170, 10, 200, 5, 70]
tipos = ['BONOS', 'CEDEAR', 'MEP', 'CEDEAR', 'MEP', 'BONOS']

instrumento_max = None

monto_min = None

acumulador_cedear = 0
contador_cedear = 0 

while True:

    # NOMBRE (Validado si se ingresa un numero)
    nombre = input('Nombre del usuario: ')
    while not nombre.isalpha():
        nombre = input('Ingrese un nombre valido: ')

    # MONTO (Validado si se ingresa una letra o un numero menor que 10.000 incluyente)
    monto_pesos = input('Ingrese el monto en pesos de la operacion(No menor a $10.000): ')

    while monto_pesos.isalpha() or int(monto_pesos) < 10000:
        monto_pesos = input('Ingrese el monto en pesos de la operacion valido (valor numerico no menor que $10.000): ')

    monto_pesos = int(monto_pesos)

    # CANTIDAD INSTRUMENTOS (Validado si se ingresa una letra o un numero negativo menor a 0)
    cantidad_instrumentos = input('Ingrese la cantidad de instrumentos operados: ')

    while cantidad_instrumentos.isalpha():
        cantidad_instrumentos = input('Ingrese una cantidad valida de instrumentos operados (valor numerico): ')
    while int(cantidad_instrumentos) > 0:
        cantidad_instrumentos = input('Ingrese una cantidad valida de instrumentos operados (mayor que 0): ')

    cantidad_instrumentos = int(cantidad_instrumentos)

    # TIPO INSTRUMENTOS (validado si se ingresa cualquier valor que no sea 'CEDEAR', 'BONO' O 'MEP')
    tipo = input('Ingrese el tipo de instrumento operado (CEDEAR, BONOS, MEP): ')

    while tipo not in ['CEDEAR', 'BONOS', 'MEP']:
        tipo = input('Ingrese un tipo de instrumento operado valido (CEDEAR, BONOS, MEP): ')

    nombres.append(nombre)
    montos.append(monto_pesos)
    instrumentos.append(cantidad_instrumentos)
    tipos.append(tipo)

    # confirmacion (validado si se ingresa cualquier valor que no sea 'si' o 'no)
    confirmacion = input('desea continuar (si/no): ')
    while confirmacion not in ['si', 'no']:
        confirmacion = input('desea continuar ingrese unicamente (si o no): ')

    if confirmacion == 'no':
        break

print('|Nombre | Monto | Cantidad | Tipo |')
print( '|---------------------------------|')
for i in range(len(nombres)):
    print( f'| {nombres[i]} | {montos[i]} | {instrumentos[i]} | {tipos[i]} |')
print( '|---------------------------------|')

# C) Realizar los siguientes informes:

# 1. Tipo de instrumento que más se operó.
for i in range(len(instrumentos)):
    if instrumento_max is None or instrumentos[i] > instrumento_max:
        instrumento_max = instrumentos[i]
        tipo_max = tipos[i]
        
print(f'El tipo de instrumento que mas se opero fue {tipo_max} con {instrumento_max} instrumentos')

contador_mas150_bonos = sum(
    instrumentos[i] <= 200
    and instrumentos[i] >= 150
    and tipos[i] == 'BONOS'
    and montos[i] > 50000
    for i in range(len(instrumentos))
)
print(f'{contador_mas150_bonos} usuarios compraron entre 150 y 200 BONOS con un valor de mas de $50000') 

# 3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno. (No tiene en cuenta que puede ser mas de uno)
for i in range(len(nombres)):

    if tipos[i] in ['BONOS', 'MEP'] and (monto_min is None or montos[i] < monto_min):
        monto_min = montos[i]
        nombre_min = nombres[i]
        instrumento_min = instrumentos[i]
print(f'{nombre_min} tiene {instrumento_min} instrumentos en forma de BONOS O MEP y es quien menos dinero invirtio con ${monto_min} de inversion')

# 4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio (No muestra mensaje cuando no hay montos que superen el promedio)
for i in range(len(nombres)):

    if tipos[i] == 'CEDEAR':
        acumulador_cedear += montos[i]
        contador_cedear += 1
if contador_cedear > 0:
    promedio_cedear = acumulador_cedear / contador_cedear
    for i in range(len(nombres)):
        if montos[i] > promedio_cedear:
            print(f'{nombres[i]} invirtio en CEDEARS y su inversion ({montos[i]}) supera el promedio {promedio_cedear}')

else:
    print('No hay inversiones en CEDEARS')

# 5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.


