from data_stark import lista_personajes
from funciones_3 import *

contador = 0

while True:  
    
    line()
    menu_input = input('1 para sanitizar datos. 2. ESC \n Ingresa una opcion:')
    line()
    
    if menu_input == '1':
        
        estado_normalizacion_fuerza = stark_normalizar_datos(lista_personajes, "fuerza", "int")
        
        estado_normalizacion_altura = stark_normalizar_datos(lista_personajes, "altura", "float")
        
        estado_normalizacion_peso = stark_normalizar_datos(lista_personajes, "peso", "float")
        
        contador += 1
        
        if contador == 1:
            
            print("Datos normalizados")
            
        else:
            
            print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
        
        
        
    elif menu_input == 'ESC':
        
        break
    
    else:
        
        print('Ingrese un opcion valido')