'''
nombre: Tomas
apellido: del Rio

Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:

-en Invierno: Bariloche tiene un aumento del 20% 
                Cataratas y Córdoba tiene un descuento del 10% 
                Mar del Plata tiene un descuento del 20%

-en Verano: Bariloche tiene un descuento del 20% 
            Cataratas y Córdoba tiene un aumento del 10% 
            Mar del Plata tiene un aumento del 20%

-en Otoño y Primavera: Bariloche tiene un aumento del 10% 
                    Cataratas tiene un aumento del 10% 
                    Mar del Plata tiene un aumento del 10% y 
                    Córdoba tiene el precio sin descuento.

Validar el ingreso de datos
'''

aumento = 0
descuento = 0
estadia_base = 15000

while aumento == 0 and descuento == 0:
    
    while True:
        estacion = input('Ingrese la estacion del año que va vacacionar (Invierno/Verano/Otoño/Primavera)')
        
        if estacion != 'Invierno' and estacion != 'Verano' and estacion != 'Otoño' and estacion != 'Primavera':
            print('Ingrese una estacion valida')
        else:
            break
        
    while True:
        localidad = input('Ingrese la localidad de destino (Bariloche/Cataratas/Mar del Plata/Córdoba)')

        if localidad != 'Bariloche' and localidad != 'Cataratas' and localidad != 'Mar delPlata' and localidad != 'Córdoba':
            print('Ingrese una localidad valida')
        else:
            break

    match estacion:
        case 'Invierno':
            if localidad == 'Bariloche':
                aumento = 20
            elif localidad == 'Cataratas' or localidad == 'Cordoba':
                descuento = 10
            elif localidad == 'Mar del Plata':
                descuento = 20
            else:
                print('Ingrese una localidad valida')
        case 'Verano':
            if localidad == 'Bariloche':
                descuento = 20
            elif localidad == 'Cataratas' or localidad == 'Cordoba':
                aumento = 10
            elif localidad == 'Mar del Plata':
                aumento = 20
        case 'Otoño' | 'Primavera':
            if localidad == 'Bariloche':
                aumento = 10
            elif localidad == 'Cataratas':
                aumento = 10
            elif localidad == 'Mar del Plata':
                aumento = 10
            
if descuento > 0:
    precio_descuento = (estadia_base / 100) * descuento
    precio_final = estadia_base - precio_descuento
    
elif aumento > 0:
    precio_aumento = (estadia_base / 100) * aumento
    precio_final = precio_aumento + estadia_base

print(f'el precio del viaje a {localidad} en {estacion} es de $ {precio_final}')

##########################################################################