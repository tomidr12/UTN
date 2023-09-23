"""
Nombre: Tomas
Apellido: del Rio
"""

from data_stark import lista_personajes


def linea():
    print("-----------------------------------------------")


def imprimir_dato(lista: list, key_parametro: str, condicion: str, key_a_visualizar: str) -> str:
    for heroe in lista:
        if heroe[key_parametro] == condicion:
            print(f'--> {heroe[key_a_visualizar]} | {heroe[key_parametro]}')


def buscador_maxmin(lista: list, key_acomparar: str, max_o_min: str, key_parametro, condicion) -> list[dict]:
    
        lista_max_min = []
        valor = None

        for heroe in lista:
            if heroe[key_parametro] == condicion:
                
                if (max_o_min == "maximo" and (valor == None or (float(heroe[key_acomparar]) > float(valor[key_acomparar])))) or (max_o_min == "minimo" and (valor == None or float(heroe[key_acomparar]) < float(valor[key_acomparar]))):
                        valor = heroe
                        
        for heroe in lista:
            if heroe[key_parametro] == condicion:
                if float(valor[key_acomparar]) == float(heroe[key_acomparar]):
                    lista_max_min.append(heroe)

        return lista_max_min


def buscador_promedio(lista: list, key_apromediar: str, key_parametro: str, condicion) -> float:
    acumulador = 0
    contador = 0
    for heroe in lista:
        if heroe[key_parametro] == condicion:
            peso = float(heroe[key_apromediar])
            acumulador += peso
            contador += 1

    if contador != 0:
        promedio = acumulador / contador
        return promedio
    else:
        return False


def cantidad_misma_caracteristica(lista: list, key_parametro: str) -> tuple[list, dict]:
    lista_parametro = []

    for heroe in lista:
        lista_parametro.append(heroe[key_parametro])

    repeticiones = {}

    for valor in lista_parametro:

        if valor == '' or valor == 'No Hair':
            valor = 'Sin pelo'

        valor = valor.capitalize()

        if valor in repeticiones:
            repeticiones[valor] += 1
        else:
            repeticiones[valor] = 0

    resultado = []
    
    for key in repeticiones:
        repeticiones[key] += 1
        resultado.append(key)

    return resultado, repeticiones


def agrupacion(lista: list, key_a_agrupar: str, key_dato_relacionado: str):

    dato_relacionado = []
    lista_colores = []

    for heroe in lista:
        if heroe[key_a_agrupar] == '' or heroe[key_a_agrupar] == 'No Hair':
            heroe[key_a_agrupar] = 'Sin pelo'

        lista_colores.append(heroe[key_a_agrupar])
        dato_relacionado.append(heroe[key_dato_relacionado])

    resultado = cantidad_misma_caracteristica(lista, key_a_agrupar)[0]

    for indice in range(len(resultado)):

        for i in range(len(lista_colores)):

            lista_colores[i] = lista_colores[i].capitalize()

            if resultado[indice] == lista_colores[i]:

                print(f'{dato_relacionado[i]} | {lista_colores[i]}')


while True:

    linea()
    menu_input = input(f' 1-Nombre de cada superheroe del genero NB \n 2-Cual es el superheroe mas alto del genero F \n 3-Cuanto es el superheroe mas alto del genero M \n 4-Cual es el superheroe mas debil del genero M \n 5-Cual es el superheroe mas debil del genero NB \n 6-Promedio de fuerza del genero NB \n 7-Cantidad de cada tipo de color de ojos \n 8-Cantidad de cada tipo de color de pelo \n 9-Superheroes agrupados por color de ojos \n 10-Superheroes agrupados por tipo de inteligencia \n 11- Salir \n Ingrese el valor deseado: ')
    linea()

    match menu_input:
        
        case '1':

            imprimir_dato(lista_personajes, "genero", "NB", "nombre")

        case '2':

            lista_personajes_femenino_altura_max = buscador_maxmin(
                lista_personajes, "altura", "maximo", "genero", "F")

            for heroe in lista_personajes_femenino_altura_max:
                print(
                    f'--> {heroe["nombre"]} es el superheroe mas alto del genero femenino, mide {heroe["altura"]}')

        case '3':

            lista_personajes_masculino_altura_max = buscador_maxmin(
                lista_personajes, "altura", "maximo", "genero", "M")

            for heroe in lista_personajes_masculino_altura_max:
                print(
                    f'--> {heroe["nombre"]} es el superheroe mas alto del genero masculino, mide {heroe["altura"]}')

        case '4':

            lista_personajes_masculino_fuerza_min = buscador_maxmin(
                lista_personajes, "fuerza", "minimo", "genero", "M")

            for heroe in lista_personajes_masculino_fuerza_min:
                print(
                    f'--> {heroe["nombre"]} es el superheroe mas debil del genero masculino, con {heroe["fuerza"]} de fuerza')

        case '5':

            lista_personajes_nobin_fuerza_min = buscador_maxmin(lista_personajes, "fuerza", "minimo", "genero", "NB")

            for heroe in lista_personajes_nobin_fuerza_min:
                print(
                    f'--> {heroe["nombre"]} es el superheroe mas debil del genero no binario, con {heroe["fuerza"]} de fuerza')

        case '6':
            promedio = buscador_promedio(lista_personajes, "fuerza", "genero", "NB")
            
            if promedio == False:
                print('No hay heroes no binarios')
            else:
                print(f'--> El promedio del peso de los No binarios es: {promedio:0.2f}')

        case '7':

            resultado = cantidad_misma_caracteristica(
                lista_personajes, "color_ojos")[0]
            repeticiones = cantidad_misma_caracteristica(
                lista_personajes, "color_ojos")[1]
            for repetido in resultado:
                print(f' {repetido} : {repeticiones[repetido]}')

        case '8':

            resultado = cantidad_misma_caracteristica(
                lista_personajes, "color_pelo")[0]
            repeticiones = cantidad_misma_caracteristica(
                lista_personajes, "color_pelo")[1]

            for repetido in resultado:
                print(f' {repetido} : {repeticiones[repetido]}')

        case '9':

            agrupacion(lista_personajes, "color_ojos", "nombre")

        case '10':

            agrupacion(lista_personajes, "color_pelo", "nombre")

        case '11':

            break

        case _:
            print('ingrese una opcion valida')