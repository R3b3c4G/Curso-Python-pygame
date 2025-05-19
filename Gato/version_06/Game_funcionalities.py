import pygame
import time
from Configurations import Configurations
from Media import Background, TurnImage, ResultsImage, CreditsImage
from TikTacToe import TicTacToeMark

def game_events(marks_group, turn_image:TurnImage):
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    # Se declara la bandera de fin de juego.
    game_over = False


    # Se verifica los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego.

        if event.type == pygame.QUIT:   # Evento cerrar ventana.
          game_over = True

        # Responder a las pulsaciones de teclas y controlar la lógica del juego en función de la entrada del usuario.
        if event.type == pygame.KEYDOWN:
            cell_keys = {
                pygame.K_q:1,
                pygame.K_w:2,
                pygame.K_e:3,
                pygame.K_a:4,
                pygame.K_s:5,
                pygame.K_d:6,
                pygame.K_z:7,
                pygame.K_x:8,
                pygame.K_c:9
            }
            if event.key in cell_keys:
                cell_number = cell_keys[event.key]
                cell_occupied = False
                for mark in marks_group:
                    if mark.get_cell_number() == cell_number:
                        cell_occupied = True
                        break
                if not cell_occupied:
                    new_mark = TicTacToeMark(cell_number)
                    marks_group.add(new_mark)
                    turn_image.change_turn(TicTacToeMark.get_turno())



    # Se regresa la bandera.
    return game_over

def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock, background: Background, marks_group:pygame.sprite.Group, turn_image: TurnImage) -> None:
    """
    Función que administra los elemento visuales del juego.
    """
    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    # Se dibuja la marca.
    marks_group.draw(screen)

    # Se dibuja la imagen del turno.
    screen.blit(turn_image.image, turn_image.rect)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())

def check_winner(marks_group) -> tuple[bool, str]:
    """

     Función para verificar si hay un ganador o si se tiene un empate.

    """
    combinaciones_ganadoras = {
        '1': [1, 2, 3],
        '2': [4, 5, 6],
        '3': [7, 8, 9],
        '4': [1, 5, 9],
        '5': [3, 5, 7],
        '6': [1, 4, 7],
        '7': [2, 5, 8],
        '8': [3, 6, 9]
    }

    lista_numeros = []

    for mark in marks_group:
        lista_numeros.append(mark.get_cell_number())

    #Marcas de x y de o
    marcas_x = []
    marcas_o = []
    for i in range(len(lista_numeros)):
        #Esto es para cada iteracion, si es doble es de los x si no es 0 en los identificadores
        if i % 2 == 0:
            marcas_x.append(lista_numeros[i])
        else:
            marcas_o.append(lista_numeros[i])

    # Verificación X o O gana.
    # Se accede a los valores de diccionario.
    for combinacion in combinaciones_ganadoras.values():
        #Aqui se reinician los contadores
        contador_x = 0
        contador_o = 0
        #se itera en cada numero de la listas del diccionario.
        for numero in combinacion:
            #Si ese número está dentro de las marcas de los jugadores aumenta contador.
            if numero in marcas_x:
                contador_x += 1
            if numero in marcas_o:
                contador_o += 1
        #Se verifica si se ha llegado a 3.
        if contador_x == 3:
            return True, "X"
        elif contador_o == 3:
            return True, "O"


    #Si tod0 eso se completo quiere deci que es empate
    if len(lista_numeros) == 9:
        return True, "draw"

    #Por si nadie ah ganado
    return False, ""


def game_over_screen(screen:pygame.surface.Surface, clock: pygame.time.Clock, background: Background, marks_group:pygame.sprite.Group, turn_image: TurnImage, result) -> None:
    """
    Muestra la pantalla de fin de juego con efecto de parpadeo.
    """
    # Se crea la imagen del resultado.
    results_image = ResultsImage(result)
    # Se crea la imagen de créditos.
    credits_image = CreditsImage()

    # Duración del afecto.
    time_effect = Configurations.get_time_effect()
    # Tiempo en el que inicia el efecto.
    start_time = time.time()

    while time.time() - start_time < 3:  # Mostrar por 3 segundos
        current_time = pygame.time.get_ticks()
        show_result = (current_time % (time_effect * 2)) < time_effect


        background.blit(screen)
        marks_group.draw(screen)
        turn_image.blit(screen)
        credits_image.blit(screen)

        # Dibujar resultado si corresponde
        if show_result:
            screen.blit(results_image.image, results_image.rect)

        pygame.display.flip()
        clock.tick(Configurations.get_fps())