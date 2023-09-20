""" 
Nombre: Tomas
Apellido: del Rio

cargar 5 productos de prevencion de contagio con los siguientes datos:
Tipo(validar "barbijo", "jabon", "alcohol")
Precio(validar entre 100 y 300)
Cantidad de unidades(No puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el fabricante

INFORMAR:
A. Del mas caro de los barbijos la cantidad de unidades y el fabricante

B. del item con mas unidades el fabricante.

C. Cuantas unidades de jabones hay en total. 

""" 

# LISTAS:
tipos = []
precios = []
cantidad_unidades = [] 
marcas = []

productos = []

#INPUTS:

for i in range(5):
    tipo = input('Ingrese el tipo de producto que desea cargar(barbijo/jabon/alcohol): ')
    while tipo != 'jabon' and tipo != 'barbijo' and tipo != 'alcohol':
        tipo = input('Ingrese el tipo de producto valido(barbijo/jabon/alcohol): ')
        
    precio = input('Ingrese el precio del producto(entre 100 y 300): ')
    while precio.isalpha() or (int(precio) < 100 or int(precio) > 300):               # no contempla caracteres especiales
        precio = input('Ingrese un precio valido(entre 100 y 300): ')
        
    cantidad_unidad = input('Ingrese la cantidad de unidaes(al menor una unidad y no mayor que 1000 unidades): ')
    while cantidad_unidad.isalpha() or (int(cantidad_unidad) <= 0 or int(cantidad_unidad) > 1000): # no contempla caracteres especiales
        cantidad_unidad = input('Ingrese una cantidad de unidades valida(al menor una unidad y no mayor que 1000 unidades): ')

    marca = input('Ingrese el nombre de la marca o del fabricante:')

    precio = int(precio)
    cantidad_unidad = int(cantidad_unidad)

    tipos.append(tipo)
    precios.append(precio)
    cantidad_unidades.append(cantidad_unidad)
    marcas.append(marca)

for i in range(len(tipos)):
    
    producto = {}
    
    # dic[key] = value
    producto['tipo'] = tipos[i]
    producto['precio'] = precios[i]
    producto['cantidad'] = cantidad_unidades[i]
    producto['marca'] = marcas[i]
    
    productos.append(producto)

# A. Del mas caro de los barbijos la cantidad de unidades y el fabricante

precio_max = productos[0]['precio']
unidades_max = productos[0]['cantidad']
fabricante_max = productos[0]['marca']

for producto in productos:
    
    if producto['tipo'] == 'barbijo':
        
        if producto['precio'] > precio_max:
            
            precio_max = producto['precio']
            unidades_max = producto['cantidad']
            fabricante_max = producto['marca']
            
print(f'El precio maximo de barbijos es de ${precio_max}, hay {unidades_max} unidades y su fabricante es: {fabricante_max}')

# B. del item con mas unidades el fabricante.

item_max = productos[0]['cantidad']
marca_item_max = productos[0]['marca']

for producto in productos:
    
    if producto['cantidad'] > item_max:
        item_max = producto['cantidad']
        marcas_item_max = producto['marca']
        
print(f'El fabricante {marca_item_max} es quien tienen mas stock con {item_max} unidades')

# C. Cuantas unidades de jabones hay en total. 

acumulador_total_jabones = 0

for producto in productos:
    
    if producto['tipo'] == 'jabon':
        acumulador_total_jabones += producto['cantidad']
        
print(f'La cantidad total de jabones es de: {acumulador_total_jabones} unidades')

####################################################################################################################################################