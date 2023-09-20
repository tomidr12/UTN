'''
nombre: Tomas
apellido: del Rio

Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
'''     
edad = input('Ingrese una edad')
edad = int(edad)

if edad <= 17 and edad >=13:
    mensaje = 'Adolescente'
elif edad < 13:
    mensaje = 'Niño'asd
else:
    mensaje = 'Adulto'

print(mensaje)

##########################################################################