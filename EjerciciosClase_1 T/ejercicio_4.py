'''
nombre: Tomas
apellido: del Rio

Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'
'''

while True:
    edad = input('Ingrese su edad')
    edad = int(edad)
    estado_civil = input('Ingrese su estado civil (soltero/casado/viudo)')

    if edad < 18 and estado_civil != 'soltero':
        print('Es muy pequeño para NO ser soltero.')
    else:
        break

##########################################################################

