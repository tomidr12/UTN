from data_stark import lista_personajes

def line():
    print('--------------------------------')


def stark_normalizar_datos(lista:list, key:str, eleccion:str):
    
    if len(lista) != 0:
        
        for elemento in lista:
            if type(elemento[key]) != int or type(elemento[key]) != float:
                
                if eleccion == 'int':
                    elemento[key] = int(elemento[key])
                    value = True
                    
                elif eleccion == 'float':
                    elemento[key] = float(elemento[key])                     
                    value = True
            else:
                value = False
    else:
        value = False
        
    return value


def stark_normalizar_datos2(lista):
    if len(lista) != 0:
        
        for elemento in lista:
            
            if type(elemento["fuerza"]) != int and type(elemento["peso"]) != float and type(elemento["altura"]) != float:
                
                elemento["fuerza"] = int(elemento["fuerza"])
                elemento["peso"] = float(elemento["peso"])
                elemento["altura"] = float(elemento["altura"])
                value = True
                
            else:
                value = False
    else:
        value = False
        
    return value


def obtener_dato(lista:list, i:int, key:str) -> str:
    
    for elemento in lista:
        
        if key not in elemento or lista[i][key] == '' or lista[i][key] == "nombre":
            return False
        else:
            if type(lista[i][key]) == float or type(lista[i][key]) == int:
                return f"{key}: {float(lista[i][key]):0.2f}"
            else:
                return f"{key}: {lista[i][key]}"
           
            
def obtener_nombre(lista:list[dict], indice:int) -> str :
    
    for _ in lista:
        
        return f'Nombre: {lista[indice]["nombre"]}'


def obtener_nombre2(heroe):
    if len(heroe) > 0 and "nombre" in heroe:
        dato = "Nombre: {0}".format(heroe["nombre"])
    
    else:
        dato = False
    
    return dato


def obtener_nombre_y_dato(lista:list[dict], key, indice) -> str:
    
    nombre = obtener_nombre(lista_personajes, indice)
    dato = obtener_dato(lista_personajes, key, indice)
    
    if dato != False:
        return f'{nombre} | {dato}'
    else:
        return False


