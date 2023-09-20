from data import lista_bzrp 

def imprimir_tema_mas_visto():
    dic_maximo = lista_bzrp[0]
    for cancion in lista_bzrp:
        if(cancion['views'] > dic_maximo['views']):
            dic_maximo = cancion
    print(dic_maximo)
    
while True:
    print('1-Maximo \n2-Baja \n3-Salir')
    opcion = input('Opcion: ')
    if opcion == '1':
        imprimir_tema_mas_visto()
    elif opcion == '2':
        print('Baja')
    elif opcion == '3':
        break
    
# Funcion con argumentos/parametros y sin retorno
def calcular_suma(numero1:int, numero2:int):
    resultado = num1 + num2
    print('la suma es {0}'.format(resultado))
    
# Programa Principal 
num1 = input('Numero 1:')
num2 = input('Numero 2:')
calcular_suma(num1, num2)

