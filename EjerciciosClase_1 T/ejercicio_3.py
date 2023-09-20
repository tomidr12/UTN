'''
nombre: Tomas
apellido: del Rio

Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
'''

lista_numeros = []

contador = 0
contador_pares = 0
contador_impares = 0

numero_par_max = None
numero_min = None
acumulador_positivos = 0 
producto = 1


while contador != 5:
    numeros = input('Ingrese un numero')
    numeros = int(numeros)
    lista_numeros.append(numeros)
    contador += 1

for numero in lista_numeros:
    # a. Cantidad de pares e impares. 
    if numero % 2 == 0: 
        contador_pares += 1
        # c. De los pares el mayor número ingresado.
        if numero_par_max == None:
            numero_par_max = numero
        elif numero > numero_par_max:
            numero_par_max = numero
    else:
        contador_impares += 1
        
    # b. El menor número ingresado.
    if numero_min == None:
        numero_min = numero
    elif numero < numero_min: 
        numero_min = numero
    
    # d. Suma de los positivos.
    if numero > 0:
        acumulador_positivos += numero
    else:
        # e. Producto de los negativos.
            producto *= numero
        
print(f'Numeros Impares: {contador_impares} | Numeros pares: {contador_pares}')
print(f'Menor numero ingresado: {numero_min}')
print(f'Mayor numero par: {numero_par_max}')
print(f'La suma de los positivos es: {acumulador_positivos}')
print(f'Producto de los negativos: {producto}')

##########################################################################