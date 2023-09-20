'''
nombre: Tomas
apellido: del Rio

CLASE 1
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''

nombre = input('Ingrese su nombre')
sueldo = input('Ingrese su sueldo')

sueldo = int(sueldo)
sueldo_10 = (sueldo / 100 ) * 10 
sueldo_incrementado = sueldo + sueldo_10
    
print(f'el sueldo de {nombre} es de {sueldo_incrementado}')

##########################################################################