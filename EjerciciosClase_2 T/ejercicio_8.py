# sourcery skip: dict-comprehension, use-dict-items
'''
Nombre: Tomas
apellido: del Rio

Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
'''

lista_numeros = [82, 3, 49, 38, 94, 95, 92, 92, 64, 8, 75, 3, 37, 97, 12, 97, 45, 48, 78, 29, 3, 58]

repeticiones = {}
for numero in lista_numeros:
  if numero in repeticiones :
    repeticiones[numero] += 1
  else:
    repeticiones[numero] = 0

resultado = []
for key in repeticiones:  
  if repeticiones[key] != 0:
    resultado.append(key)
    
print(resultado)
print(f'Se encontraron {len(resultado)} numeros repetidos')

##########################################################################