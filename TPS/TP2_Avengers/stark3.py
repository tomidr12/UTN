"""
Nombre: Tomas
Apellido: del Rio
"""

from data_stark import lista_personajes


def stark_normalizar_datos(lista: list, key_a_normalizar: str, tipo_de_dato_a_castear):

    if len(lista) != 0:

        for elemento in lista:
            if type(elemento[key_a_normalizar]) != int or type(elemento[key_a_normalizar]) != float:

                if tipo_de_dato_a_castear == int:
                    elemento[key_a_normalizar] = int(
                        elemento[key_a_normalizar])
                    value = True

                elif tipo_de_dato_a_castear == float:
                    elemento[key_a_normalizar] = float(
                        elemento[key_a_normalizar])
                    value = True
            else:
                value = False
    else:
        value = False

    return value


def obtener_dato(lista: list, indice: int, key_a_obtener: str) -> str:

    if len(lista) != 0:

        for elemento in lista:

            if key_a_obtener not in elemento or lista[indice][key_a_obtener] == '' or lista[indice][key_a_obtener] == "nombre":

                return False

            else:

                if type(lista[indice][key_a_obtener]) == float or type(lista[indice][key_a_obtener]) == int:

                    return float(lista[indice][key_a_obtener])

                else:

                    return lista[indice][key_a_obtener]

    else:

        return False


def obtener_nombre(lista: list, indice: int) -> str:

    if len(lista) != 0:

        for elemento in lista:

            if "nombre" in elemento:

                return f'Nombre: {lista[indice]["nombre"]}'

            else:

                return False

    else:

        return False


def obtener_nombre_y_dato(lista: list, indice: int, key_a_obtener: str) -> str:

    heroe = {}
    nombre = obtener_nombre(lista, indice)
    dato = obtener_dato(lista, indice, key_a_obtener)
    
    if dato != False and nombre != False:
        heroe["nombre"] = nombre
        heroe["dato"] = dato
        return heroe
    else:
        return False


def obtener_maximo(lista: list, key_a_obtener: str) -> int | float:

    max_valor_key = None

    if len(lista) != 0:
        for elemento in lista:
            if type(elemento[key_a_obtener]) == int or type(elemento[key_a_obtener]) == float:
                if max_valor_key == None:
                    max_valor_key = elemento[key_a_obtener]
                elif max_valor_key < elemento[key_a_obtener]:
                    max_valor_key = elemento[key_a_obtener]
            else:
                return False
    else:
        return False

    return max_valor_key


def obtener_minimo(lista: list, key_a_obtener: str) -> int | float:

    min_valor_key = None

    if len(lista) != 0:
        for elemento in lista:
            if type(elemento[key_a_obtener]) == int or type(elemento[key_a_obtener]) == float:

                if min_valor_key == None:
                    min_valor_key = elemento[key_a_obtener]
                elif min_valor_key > elemento[key_a_obtener]:
                    min_valor_key = elemento[key_a_obtener]

            else:
                return False
    else:
        return False

    return min_valor_key


def obtener_dato_cantidad(lista: list, valor_a_comparar:str, key_a_obtener: str) -> list[dict]:

    lista_dato = []
    for elemento in lista:
        if elemento[key_a_obtener] == valor_a_comparar:
            lista_dato.append(elemento)

    return lista_dato


def stark_imprimir_heroes(listaheroes: list):
    if len(listaheroes) > 0:
        for heroe in listaheroes:
            print("\n{0}\n".format("=" * 50))
            for clave, valor in heroe.items():
                print("{0}: {1}".format(clave, valor))
            print("\n{0}\n".format("=" * 50))
    else:
        print(False)


def sumar_dato_heroe(lista: list, key_a_sumar: str) -> int | float:
    acumulador_dato = 0

    if len(lista) != 0:
        for elemento in lista:
            if key_a_sumar in elemento and elemento[key_a_sumar] != '' and (type(elemento[key_a_sumar]) == int or type(elemento[key_a_sumar]) == float):
                acumulador_dato += elemento[key_a_sumar]
            else:
                return False
    else:
        return False

    if acumulador_dato == 0:
        return False
    else:
        return acumulador_dato


def dividir(dividendo: int | float, divisor: int | float) -> int | float:

    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor

    return resultado


def calcular_promedio(lista: list, key_a_promediar: str) -> int | float:

    dato_sumado = sumar_dato_heroe(lista, key_a_promediar)

    promedio = dividir(dato_sumado, len(lista))

    if dato_sumado != False and promedio != False:
        return promedio
    else:
        return False


def mostrar_promedio_dato(lista: list, key_a_mostar: str) -> str:

    if len(lista) != 0:
        promedio = calcular_promedio(lista, key_a_mostar)
        if promedio == False:
            return False
        else:
            return f'{promedio:0.2f}'
    else:
        return False


def linea() -> str:
    print('------------------------------------------------')


def imprimir_menu() -> str:

    linea()
    menu_input = input(f'1. Normalizar datos \n2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB \n3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M \n6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB \n7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB \n8. Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n9. Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n10. Listar todos los superhéroes agrupados por color de ojos. \n11. Listar todos los superhéroes agrupados por tipo de inteligencia\n0-SALIR \nIngrese una opcion:')
    linea()

    return menu_input


def validar_entero(numero: str) -> bool:
    if not numero.isalpha() and numero != '' and int(numero) > 0:
        return True
    else:
        return False


def stark_menu_principal() -> int:
    
    valor_input = imprimir_menu()
    
    validacion_int = validar_entero(valor_input)
    
    if validacion_int == True:
        valor_input = int(valor_input)
    else:
        return False
        
    return valor_input
    
    
def stark_marvel_app(lista:list):
    
    contador = 0 
    
    while True:
        
        valor_input = stark_menu_principal()
        
        if valor_input == 1 and contador == 0:      
    
            contador += 1
            print("Datos normalizados")
            stark_normalizar_datos(lista, "fuerza", int)
            stark_normalizar_datos(lista, "peso", float)
            stark_normalizar_datos(lista, "altura", float)
        
        elif valor_input > 1 and contador == 0:
            print('Primero debe normalizar los datos.')
                
        elif valor_input == 1 and contador == 1:
            print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
                
        elif valor_input == 2 and contador == 1:
            lista_genero_nb = obtener_dato_cantidad(lista, "NB", "genero")
            stark_imprimir_heroes(lista_genero_nb)
            
        elif valor_input == 3 and contador == 1:
            
            lista_heroe_nb = obtener_dato_cantidad(lista, "F", "genero")
            
            heroe_mas_alta = obtener_maximo(lista_heroe_nb, "altura")
            
            heroes_mas_altas = obtener_dato_cantidad(lista, heroe_mas_alta, "altura")
            
            stark_imprimir_heroes(heroes_mas_altas)
            
        elif valor_input == 4 and contador == 1:
            
            lista_heroe_masculino = obtener_dato_cantidad(lista, "M", "genero")
            
            heroe_mas_alto = obtener_maximo(lista_heroe_masculino, "altura")
            
            heroes_mas_altos = obtener_dato_cantidad(lista, heroe_mas_alto, "altura")
            
            stark_imprimir_heroes(heroes_mas_altos)
            
        elif valor_input == 5 and contador == 1:
            
            lista_heroe_masculino = obtener_dato_cantidad(lista, "M", "genero")
            
            heroe_mas_debil_m = obtener_minimo(lista_heroe_masculino, "fuerza")
            
            heroes_mas_debiles_m = obtener_dato_cantidad(lista, heroe_mas_debil_m, "fuerza")
            
            stark_imprimir_heroes(heroes_mas_debiles_m)
            
        elif valor_input == 6 and contador == 1:
            
            lista_heroe_nb = obtener_dato_cantidad(lista, "NB", "genero")
            
            heroe_mas_debil_nb = obtener_minimo(lista_heroe_nb, "fuerza")
            
            heroes_mas_debiles_nb = obtener_dato_cantidad(lista, heroe_mas_debil_nb, "fuerza")
            
            stark_imprimir_heroes(heroes_mas_debiles_nb)
            
        elif valor_input == 7 and contador == 1:
            
            lista_heroe_nobinario = obtener_dato_cantidad(lista, "NB", "genero")

            print(f'El promedio de fuerza del genero no binario es: {mostrar_promedio_dato(lista_heroe_nobinario, "fuerza")}')
            
        elif valor_input == 8 and contador == 1:
            
            lista_colores_ojos = []
            repetidos = {}
            
            for i in range(len(lista)):
                lista_colores_ojos.append(obtener_dato(lista,i, "color_ojos").capitalize())
            
            for valor in lista_colores_ojos:

                if valor in repetidos:
                    repetidos[valor] += 1
                else:
                    repetidos[valor] = 1
            
            resultado = []
    
            for key in repetidos:
                repetidos[key] += 1
                resultado.append(key)
            
            for repetido in resultado:
                print(f' {repetido} : {repetidos[repetido]}')
                
        elif valor_input == 9 and contador == 1:
            
            lista_colores_pelo = []
            repetidos = {}
            
            for i in range(len(lista)):
                lista_colores_pelo.append(obtener_dato(lista,i, "color_pelo"))
            
            for valor in lista_colores_pelo:
                
                if valor == '' or valor == 'No Hair' or valor == False:
                    valor = 'Sin pelo'

                if valor in repetidos:
                    repetidos[valor] += 1
                else:
                    repetidos[valor] = 1
            
            resultado = []
    
            for key in repetidos:
                repetidos[key] += 1
                resultado.append(key)
            
            for repetido in resultado:
                print(f' {repetido} : {repetidos[repetido]}')   
            
        elif valor_input == 10 and contador == 1:
        
            lista_colores_ojos = []
            lista_unica_ojos = []
            
            for i in range(len(lista)):
                valor = obtener_dato(lista, i , "color_ojos").capitalize()
                lista_colores_ojos.append(valor)
            
            colores_sinrepetir = set(lista_colores_ojos)
            
            for color in colores_sinrepetir:
                lista_unica_ojos.append(color)

            for indice in range(len(lista_unica_ojos)):
                for i in range(len(lista_colores_ojos)):
                    if lista_unica_ojos[indice] == lista_colores_ojos[i]:
                        valor = obtener_nombre_y_dato(lista, i, "color_ojos")
                        print('{0} | {1}'.format(valor["nombre"], valor["dato"]))
                               
        elif valor_input == 11 and contador == 1:
            lista_tipo_inteligencia = []
            lista_unica_tipo_inteligencia = []
            
            for i in range(len(lista)):
                valor = obtener_dato(lista, i , "inteligencia")
                if valor == False:
                    valor = "Sin inteligencia"
                valor = valor.capitalize()
                lista_tipo_inteligencia.append(valor)
            
            colores_sinrepetir = set(lista_tipo_inteligencia)
            
            for color in colores_sinrepetir:
                lista_unica_tipo_inteligencia.append(color)
            
            for indice in range(len(lista_unica_tipo_inteligencia)):
                for i in range(len(lista_tipo_inteligencia)):
                    if lista_unica_tipo_inteligencia[indice] == lista_tipo_inteligencia[i]:
                        valor = obtener_nombre_y_dato(lista, i, "inteligencia")
                        if type(valor) == bool:
                            pass
                        else:
                            print('{0} | {1}'.format(valor["nombre"], valor["dato"]))
        
        elif valor_input == 0 and contador >= 0:
            break
        
        else:
            print('Ingrese un valor valido')
            
            
stark_marvel_app(lista_personajes)