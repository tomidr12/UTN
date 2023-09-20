from 'base de datos o archivo con data' import lista_bzrp

# Trae y compara un valor por vez

maximo = lista_bzrp[0]["views"]
nombre_max = lista_bzrp[0]["title"]

for dic in lista_bzrp:
    if dic["views"] > maximo:
        maximo = dic["views"]
        nombre_max = dic["title"]

print (f' {nombre_max} | con {maximo} views')

# Compara un valor y trae todo el diccionario
dic_maximo = lista_bzrp[0]

for e_lista in lista_bzrp:
    if (e_lista["views"] > dic_maximo["views"]):
        dic_maximo = e_lista

print (f' La sesion {dic_maximo["title"]} tiene {dic_maximo["views"]} views')