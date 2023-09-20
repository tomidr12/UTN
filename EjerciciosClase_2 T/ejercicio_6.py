'''
Nombre: Tomas
apellido: del Rio

Ejercicio 6:
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.
'''

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 120, 55, 48, 78, 29, 58]

mayor = lista_numeros[0]

for numero in lista_numeros:
    if mayor < numero:
        mayor = numero
        
print(mayor)

##########################################################################

