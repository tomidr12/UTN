'''
Nombre: Tomas
Apellido: del Rio 

Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
'''


nombres = ["Juan", "Pedro", "Sol", "Paco", "Ana"]
sexos = ["f", "f", "f", "f", "f"]
notas = [10, 8, 10, 7, 10]

acumulador_notas_mujeres = 0
contador_mujeres = 0

flag = True
menor = notas[0]

for _ in range(5):
    nombre = input('Ingrese el nombre del alumno')
    while nombre.isdigit():
        nombre = input('Ingrese un nombre valido')

    genero = input('Ingrese el genero del alumno (f/m)')
    while genero != 'f' and genero != 'm':
        genero = input('Ingrese un genero valido (f/m)')

    nota = input('Ingrese la nota del alumno')
    while not nota.isdigit():
        nota = input('Ingrese una nota valida(caracter numerico)')
    while int(nota) < 0 or int(nota) > 10:
        nota = input('Ingrese una nota valida (entre 0 y 10): ')

    nota = int(nota)

    nombres.append(nombre)
    sexos.append(genero)
    notas.append(nota)

    print('alumno cargado con exito')
# Mostrar el nombre del hombre con nota más baja


for i in range(len(nombres)):

    if sexos[i] == 'm' and flag or notas[i] < menor:
        flag = False
        menor = notas[i]
        nombre_menor = nombres[i]

    if sexos[i] == 'f':
        acumulador_notas_mujeres += notas[i]
        contador_mujeres += 1
if flag == False:
    print(f'El nombre del alumno con menor nota es {nombre_menor}')
else:
    print('no hay alumnos hombres')

# Mostrar el promedio de notas de las mujeres
if contador_mujeres != 0:
    promedio_notas_mujeres = acumulador_notas_mujeres / contador_mujeres
    print(f'El promedio de las notas de las mujeres es: {promedio_notas_mujeres}')
else:
    print('no hay alumnas mujeres')


##########################################################################
