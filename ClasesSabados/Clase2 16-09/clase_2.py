import random

def validar_entero(numero:int):
    if int(numero) >= -500 and int(numero) <= 500:
        return True
    else:
        return False
    
def list_random():
    lista_numeros = []
    
    for _ in range(20):
        numero_random = random.randint(-1000, 1000)
        lista_numeros.append(numero_random)
    
    return lista_numeros

numero_input = None

while True:
    
    print("-----------------------------------------------")
    menu_input = input(f'1-Pedir numero entero \n2-Validar que el numero este entre -500 y 500 \n3-Generar una lista con 20 numeros aleatorios entre el -1000 y el 1000 pero agregar a la lista solamente los numeros entre -500 y 500')
    print("-----------------------------------------------")

    match menu_input:
        
        case '1':
            
            numero_input = input(f'Ingrese un numero entero: ')
        
        case '2':
            
            if numero_input == None:
                
                numero_input = input(f'Ingrese un numero entero: ')              
                  
            else:
                
                validacion_rango = validar_entero(numero_input)
                
                if validacion_rango:
                    print(f"El numero {int(numero_input)} esta entre -500 y 500")
                else:
                    print(f"El numero {int(numero_input)} no esta entre -500 y 500")
            