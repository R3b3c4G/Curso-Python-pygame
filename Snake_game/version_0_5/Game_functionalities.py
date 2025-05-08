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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)
    # Se regresa la bandera
    return game_over

def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Función que gestiona el movimiento del cuerpo de la serpiente.
    :param snake_body:
    :return:
    """
    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()


def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group) -> None:
    """
    Función que administra los elemento visuales del juego.
    :return:
    """
    screen.fill(Configurations.get_background())

    # S dibuja el cuerpo de la serpiente.
    for snake_block in snake_body.sprites():
        snake_block.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())
