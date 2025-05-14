import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark

def game_events() -> bool:
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

    # Se regresa la bandera
    return game_over


def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock, background: Background) -> None:
    """
    Función que administra los elemento visuales del juego.
    """
    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())