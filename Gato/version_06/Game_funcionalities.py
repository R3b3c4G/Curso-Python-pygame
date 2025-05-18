import pygame
from Configurations import Configurations
from Media import Background, TurnImage
from TikTacToe import TicTacToeMark

def game_events(marks_group, turn_image:TurnImage) -> bool:
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

def check_winner(marks_group) -> bool|str:
    """
    Función para verificar si hay un ganador o si se tiene un empate.
    """
    combinaciones_ganadoras = {'1':[1,2,3],
                               '2':[4,5,6],
                               '3':[7,8,9],
                               '4':[1,5,9],
                               '5':[3,5,7]}
    contador_de_marcas = 0
    lista_numeros = []
    game_over = False
    for mark in marks_group:
        lista_numeros.append(mark.get_cell_number)
    lista_numeros = lista_numeros.reverse()

    #For que itera de dos en dos:
    for i in range(0, len(marks_group), 2):
        for key, value in combinaciones_ganadoras.items():
            if lista_numeros[i] in value:
                contador_de_marcas +=1
            else:
                contador_de_marcas = 0
            
        if contador_de_marcas == 3:
            ganador = "x"
            game_over = True
            return game_over, ganador

    return game_over
