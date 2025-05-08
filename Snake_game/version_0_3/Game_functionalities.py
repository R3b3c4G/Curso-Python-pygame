import pygame
from Configuration import Configurations
from Snake import SnakeBlock

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


def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock, snake_head: SnakeBlock) -> None:
    """
    Función que administra los elemento visuales del juego.
    :return:
    """
    screen.fill(Configurations.get_background())

    # S dibuja la cabeza de la serpiente.
    snake_head.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())
