import operator
from data_bzrp import lista_bzrp

# ⦁	Recorrer la lista imprimiendo por consola el título de cada video

for video in lista_bzrp:
    print(video["title"])
    
# ⦁	Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo

for video in lista_bzrp:
    print(f'{video["title"]} | {video["views"]} views')

# ⦁	Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)

views_max = lista_bzrp[0]["views"]

for video in lista_bzrp:
    if video["views"] > views_max:
        views_max = video["views"]

print(f'Cantidad maxima de reproducciones {views_max}')

# ⦁	Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)

views_min = lista_bzrp[0]["views"]

for video in lista_bzrp:
    if video["views"] < views_min:
        views_min = video["views"]

print(f'Cantidad mínima de reproducciones {views_min}')

# ⦁	Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)
acumulador_views = 0 

for video in lista_bzrp:
    acumulador_views += video["views"]
    
print(f'Cantidad total de reproducciones: {acumulador_views}')

# ⦁	Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)

acumulador_views = 0 

for video in lista_bzrp:
    acumulador_views += video["views"]

promedio_views = acumulador_views / len(lista_bzrp)
    
print(f'Cantidad promedio de reproducciones: {promedio_views:.2f}')

# ⦁	Informar cual es el Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)

views_max = lista_bzrp[0]["views"]
nombre_views_max = lista_bzrp[0]["title"]

views_min = lista_bzrp[0]["views"]
nombre_views_min = lista_bzrp[0]["title"]

acumulador_views = 0 

for video in lista_bzrp:
    
    acumulador_views += video["views"]
    
    if video["views"] > views_max:
        views_max = video["views"]
        nombre_views_max = video["title"]
    
    elif video["views"] < views_min:
        views_min = video["views"]
        nombre_views_min = video["title"]
        
        
promedio_views = acumulador_views / len(lista_bzrp)

print(f'La cancion con mas reproducciones es {nombre_views_max} con {views_max} views')\
    
print(f'La cancion con menos reproducciones es {nombre_views_min} con {views_min} views')

for video in lista_bzrp:
    if video["views"] > promedio_views:
        print(f'La cancion {video["title"]} supera el promedio({promedio_views:.2f}) de views con {video["views"]} views')
    else:
        print(f'La cancion {video["title"]} NO supera el promedio({promedio_views:.2f}) de views con {video["views"]} views')

print(f'La cantidad total de reproducciones de todos los videos es: {acumulador_views}')

# ⦁	Calcular e informar cual es el video que más y el que menos dura.

duracion_max = lista_bzrp[0]["length"]
nombre_duracion_max = lista_bzrp[0]["title"]

duracion_min = lista_bzrp[0]["length"]
nombre_duracion_min = lista_bzrp[0]["title"]

for video in lista_bzrp:
    if video["length"] > duracion_max:
        duracion_max = video["length"]
        nombre_duracion_max = video["title"]
        
    elif video["length"] < duracion_min:
        duracion_min = video["length"]
        nombre_duracion_min = video["title"]
         
print(f'El video que mas dura es {nombre_duracion_max} con una duracion de {duracion_max} segundos')

print(f'El video que menos dura es {nombre_duracion_min} con una duracion de {duracion_min} segundos')

# ⦁	Ordenar el código implementando una función para cada uno de los valores informados

    # hacer una lista nueva trayendo solo los dates con el valor del indice de cada uno, despues ordenarlos y depsues nombrar cada video usando el indice de cada date para traer el dato del nombre

    # diccionario[indice] = value

""" lista_dates = []

for videos in lista_bzrp:
    lista_dates.append(videos["date"])

print(lista_dates)

dates_orden = {}
for i in range(len(lista_dates)):
    dates_orden[i] = lista_dates[i]

print(dates_orden) """ # No me termino de salir


lista_bzrp.sort(key = operator.itemgetter('date'))

for video in lista_bzrp:
    print(f'{video["title"]} | {video["date"]}')

# ⦁	Construir un menú que permita elegir qué dato obtener

eleccion_usuario = input('Que tipo de dato quiere ver (titulo/views/duracion/url/fecha/imagen): ')

while eleccion_usuario not in ['titulo', 'views', 'duracion', 'url', 'fecha', 'image']:
    eleccion_usuario = input('Ingrese un dato valido (titulo/views/duracion/url/fecha/imagen): ')

for video in lista_bzrp:
    match eleccion_usuario:
        case 'titulo':
                print(video["title"])
                
        case 'views':
                print(video["views"])
                
        case 'duracion':
                print(video["length"])
                
        case 'url':                                                             
                print(video["url"])
                
        case 'fecha':
                print(video["date"])
                
        case 'imagen':
                print(video["image"])
            

