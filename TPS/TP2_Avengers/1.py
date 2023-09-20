from data_stark import lista_personajes


for elemento in lista_personajes:
    if type(elemento["fuerza"]) != float:
        elemento["fuerza"] = float(elemento["fuerza"])
        
print(lista_personajes)