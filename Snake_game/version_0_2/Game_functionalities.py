import pygame
from Configuration import Configurations
def game_events() -> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    # Se declara la bandera del sin del juego.
    game_over = False


    # Se verifica los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego.
        if event.type == pygame.QUIT:   # Evento cerrar ventana.
          game_over = True

    # Se regresa la bandera
    return game_over


def screen_refresh(screen:pygame.surface.Surface) -> None:
    """
    Función que administra los elemento visuales del uego.
    :return:
    """
    screen.fill(Configurations.get_background())

    # Se actualiza la pantalla.
    pygame.display.flip()

