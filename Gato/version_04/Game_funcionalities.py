import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark

def game_events(marks_group) -> bool:
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
            if event.key == pygame.K_q:
                new_mark = TicTacToeMark(1)
                marks_group.add(new_mark)

            elif event.key == pygame.K_w:
                new_mark = TicTacToeMark(2)
                marks_group.add(new_mark)

            elif event.key == pygame.K_e:
                new_mark = TicTacToeMark(3)
                marks_group.add(new_mark)

            elif event.key == pygame.K_a:
                new_mark = TicTacToeMark(4)
                marks_group.add(new_mark)

            elif event.key == pygame.K_s:
                new_mark = TicTacToeMark(5)
                marks_group.add(new_mark)

            elif event.key == pygame.K_d:
                new_mark = TicTacToeMark(6)
                marks_group.add(new_mark)

            elif event.key == pygame.K_z:
                new_mark = TicTacToeMark(7)
                marks_group.add(new_mark)

            elif event.key == pygame.K_x:
                new_mark = TicTacToeMark(8)
                marks_group.add(new_mark)

            elif event.key == pygame.K_c:
                new_mark = TicTacToeMark(9)
                marks_group.add(new_mark)

    # Se regresa la bandera
    return game_over


def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock, background: Background, marks_group:pygame.sprite.Group) -> None:
    """
    Función que administra los elemento visuales del juego.
    """
    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    # Se dibuja la marca.
    marks_group.draw(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())