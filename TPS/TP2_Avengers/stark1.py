"""
Nombre: Tomas
Apellido: del Rio
"""

from data_stark import lista_personajes


def linea() -> str:
    print("-----------------------------------------------")


def datos_personaje() -> str:
    for superheroe in lista_personajes:
        print("--> {0}".format(superheroe))


def buscado_maxmin(lista: list, key_acomparar: str, max_o_min: str) -> list[dict]:

    if max_o_min == "maximo":
        lista_maximo = []
        valor_maximo = None

        for heroe in lista:
            if valor_maximo == None or (float(heroe[key_acomparar]) > float(valor_maximo[key_acomparar])):
                valor_maximo = heroe

        for heroe in lista:
            if float(valor_maximo[key_acomparar]) == float(heroe[key_acomparar]):
                lista_maximo.append(heroe)

        return lista_maximo

    if max_o_min == 'minimo':
        lista_minimo = []
        valor_minimo = None

        for heroe in lista:
            if valor_minimo == None or (float(heroe[key_acomparar]) < float(valor_minimo[key_acomparar])):
                valor_minimo = heroe

        for heroe in lista:
            if float(valor_minimo[key_acomparar]) == float(heroe[key_acomparar]):
                lista_minimo.append(heroe)

        return lista_minimo


def buscador_promedio(lista: list, key_apromediar: str, condicion1: str, parametro: str) -> float:
    acumulador = 0
    contador = 0
    for heroe in lista:
        if heroe[condicion1] == parametro:
            valor = float(heroe[key_apromediar])
            acumulador += valor
            contador += 1

    promedio_valor = acumulador / contador
    return promedio_valor


while True:

    linea()
    menu_input = input(f'ingrese la opcion que desee: \n 1-Los datos de cada superheroe: \n 2-Identidad y Peso del superheroe de mayor fuerza \n 3-Nombre e identidad del superheroe mas bajo \n 4-Peso promedio de los superheroes masculinos \n 5-Nombre y Peso de los superheroe los cuales su fuerza supere la fuerza promedio de todas las superheroes de genero femenino \n 6-Salir \n Ingresar valor: ')

    match menu_input:
        
        case '1':
            
            linea()
            datos_personaje()
            
        case '2':
            
            linea()

            lista_personajes_mayor_fuerza = buscado_maxmin(
                lista_personajes, "fuerza", "maximo")

            for heroe in lista_personajes_mayor_fuerza:
                print(
                    f'--> {heroe["identidad"]} con {float(heroe["peso"]):0.2f}kg es el superheroe de mayor fuerza con {float(heroe["fuerza"]):0.2f} puntos')

        case '3':

            linea()

            lista_personajes_mas_alto = buscado_maxmin(
                lista_personajes, "altura", "minimo")

            for heroe in lista_personajes_mas_alto:
                print(
                    f'--> {heroe["nombre"]} su identidad es: {heroe["identidad"]} y es el superheroe mas bajo con {float(heroe["altura"]):0.2f}cms')

        case '4':

            linea()
            promedio = buscador_promedio(
                lista_personajes, "peso", "genero", "M")
            print(
                f'--> El promedio del peso de los hombres es: {promedio:0.2f}')

        case '5':

            linea()
            promedio_fuerza_femenino = float(buscador_promedio(lista_personajes, "fuerza", "genero", "F"))

            for heroe in lista_personajes:
                if float(heroe["fuerza"]) > promedio_fuerza_femenino:
                    print(f'--> {heroe["nombre"]} | {float(heroe["peso"]):0.2f}kg | {"fuerza"} : {heroe["fuerza"]} | supera el promedio de {"fuerza"} femenino')

        case '6':
            
            break
        
        case _:
            
            linea()
            print('Ingrese una opcion valida.')