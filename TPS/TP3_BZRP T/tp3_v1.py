import pygame
from data_bzrp import lista_bzrp
from constantes import *
titulo = ""
lista_titulos = []

posicion = 0

for e_lista in lista_bzrp:
    lista_titulos.append(e_lista["title"])

pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Primer Pygame")

imagen = pygame.image.load("../../Recursos/UTN.png")

imagen = pygame.transform.scale(imagen, (800, 600))
fuente = pygame.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_GRIS)

running = True

while running:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = evento.pos

            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120 ):

                titulo = lista_titulos[posicion]
                texto_titulo = fuente.render(str(titulo), True, COLOR_BLANCO)

                if posicion > len(lista_titulos):
                    posicion = 0
                else:
                    posicion = posicion + 1



    pantalla.fill(COLOR_ROJO)
    # Fundimos la imagen en la superficie de la pantalla
    # pantalla.blit(imagen, (0, 0),)
    pygame.draw.rect(pantalla, COLOR_BLANCO, (300,20,200,100)) #LEFT, TOP, ANCHO Y ALTO

    pantalla.blit(texto_titulo, (150, 150))
    pygame.display.flip()


######################################################################

# pygame.init() # Se inicializa pygame

# screen = pygame.display.set_mode([500,500]) # Se crea la ventana
# running = True

# while running:
#     # Se verifica si el usuario cerro la ventana
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255,255,255)) # se pinta el fondo de la ventana

#     # Se dibuja un circulo azul en el centro
#     pygame.draw.circle(screen, (0,0,255), (250,250), 75)

#     pygame.display.flip() # Muestra los cambios en la pantalla

# pygame.quit() # Fin del programa
