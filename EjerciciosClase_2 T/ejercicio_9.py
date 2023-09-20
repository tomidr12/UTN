'''
Nombre: Tomas
apellido: del Rio

Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
'''

edades = [25,36,145,23,45]
nombres = ["Juan","Ana","Sol","Mario","Sonia"]

edad_min = edades[0]
nombre = nombres[0]

for i in range(len(nombres)):
    edad = edades[i]
    
    if edad_min >= edad:
        edad_min = edad
        nombre = nombres[i]
        
print(f'{nombre} es la persona mas joven')

##########################################################################