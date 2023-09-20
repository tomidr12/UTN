"""
Nombre: Tomas
Apellido: del Rio
"""

from datos import lista
import pygame
from constantes import *

#Sub-Listas
lista_vacia = ['']
lista_preguntas = []
lista_opciones_a = []
lista_opciones_b = []
lista_opciones_c = []
lista_respuesta_correcta = []

#Inicializadores
error = -1
pregunta = ''
opcion_a = ''
opcion_b = ''
opcion_c = ''
eleccion = ''
posicion = 0
score = 0

for desafio in lista:
    lista_preguntas.append(desafio['pregunta'])
    lista_opciones_a.append(desafio['a'])
    lista_opciones_b.append(desafio['b'])
    lista_opciones_c.append(desafio['c'])
    lista_respuesta_correcta.append(desafio['correcta'])


def renderizado(lista:list, indice, font):
    opcion = lista[indice]
    valor_renderizado = font.render(str(opcion), True, COLOR_BLANCO)
    return valor_renderizado

pygame.init()
# Ventana y titulo
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Preguntados UTN')

# Fuente
fuente = pygame.font.SysFont("Arial", 30)

# Pregunta
texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)

# Score
texto_score = fuente.render('SCORE: ' + str(score), True, COLOR_BLANCO)

# Opciones
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)

# Botones
texto_btn_pregunta = fuente.render('PREGUNTA', True, COLOR_NEGRO)
texto_btn_reinicio = fuente.render('REINICIO', True, COLOR_NEGRO)

# Logo
imagen_logo = pygame.image.load(
    'recursos/logo.jpeg')
imagen_logo = pygame.transform.scale(imagen_logo, (200, 200))

# Flag
running = True

while running:

    lista_eventos = pygame.event.get()

    # Quit
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = evento.pos

            # Boton Pregunta
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):

                if posicion > len(lista_preguntas) - 1:
                    print('llegaste al final, vas a volver a comenzar')
                    posicion = 0
                
                error = -1
                
                eleccion = ''
                
                texto_pregunta = renderizado(lista_preguntas, posicion, fuente)

                texto_opcion_a = renderizado(lista_opciones_a, posicion, fuente)

                texto_opcion_b = renderizado(lista_opciones_b, posicion, fuente)

                texto_opcion_c = renderizado(lista_opciones_c, posicion, fuente)

                posicion = posicion + 1

            # Boton Reinicio
            elif (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 480 and posicion_click[1] < 580):
                
                eleccion = ''
                posicion = 0
                score = 0
                error = -1
                
                texto_score = fuente.render('SCORE: ' + str(score), True, COLOR_BLANCO)
                
                texto_pregunta = renderizado(lista_preguntas, posicion, fuente)

                texto_opcion_a = renderizado(lista_opciones_a, posicion, fuente)

                texto_opcion_b = renderizado(lista_opciones_b, posicion, fuente)

                texto_opcion_c = renderizado(lista_opciones_c, posicion, fuente)
                
                posicion = posicion + 1

            # Opciones
            if (posicion_click[0] > 10 and posicion_click[0] < 210) and (posicion_click[1] > 375 and posicion_click[1] < 425):

                eleccion = 'a'

            elif (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 375 and posicion_click[1] < 425):

                eleccion = 'b'

            elif (posicion_click[0] > 590 and posicion_click[0] < 790) and (posicion_click[1] > 375 and posicion_click[1] < 425):

                eleccion = 'c'

            # Evaluacion respuesta correcta
            if lista_respuesta_correcta[posicion-1] == eleccion:

                print('correcta')

                if score >= 991:

                    texto_score = fuente.render('GANASTE', True, COLOR_BLANCO)
                    
                    eleccion = ''
                    posicion = 0
                    score = 0
                    error = -1

                else:
                    
                    if posicion > len(lista_preguntas) - 1:
                        print('llegaste al final, vas a volver a comenzar')
                        posicion = 0
                        
                    score = score + 10

                    texto_score = fuente.render('SCORE: ' + str(score), True, COLOR_BLANCO)
                        
                    error = -1

                    eleccion = ''
                    
                    texto_pregunta = renderizado(lista_preguntas, posicion, fuente)

                    texto_opcion_a = renderizado(lista_opciones_a, posicion, fuente)

                    texto_opcion_b = renderizado(lista_opciones_b, posicion, fuente)

                    texto_opcion_c = renderizado(lista_opciones_c, posicion, fuente)

                    posicion = posicion + 1
            
            else:
                
                error += 1
                
                if error == 2: 
                    
                    texto_opcion_a = renderizado(lista_vacia, 0, fuente)

                    texto_opcion_b = renderizado(lista_vacia, 0, fuente)

                    texto_opcion_c = renderizado(lista_vacia, 0, fuente)
                    
                    posicion = posicion + 1
                    
                    error = -1

    # Background
    pantalla.fill(COLOR_AZUL_OSCURO)

    # botones
    # LEFT, TOP, ANCHO Y ALTO
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 20, 200, 100))
    pantalla.blit(texto_btn_pregunta, (320, 55))
    
    # LEFT, TOP, ANCHO Y ALTO
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 480, 200, 100))
    pantalla.blit(texto_btn_reinicio, (333, 515))

    # score
    pantalla.blit(texto_score, (300, 150))

    # pregunta
    pantalla.blit(texto_pregunta, (10, 250))

    # opciones
    # A
    pantalla.blit(texto_opcion_a, (10, 375))
    
    # B
    pantalla.blit(texto_opcion_b, (300, 375))

    # C
    pantalla.blit(texto_opcion_c, (590, 375))

    # Logo
    pantalla.blit(imagen_logo, (10, 10))

    # Actualizacion
    pygame.display.flip()

pygame.quit()