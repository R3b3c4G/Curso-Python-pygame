import time

import pygame
from Configuration import Configurations
from Snake import SnakeBlock
from Apple import Apple
from media import Background, Audio


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
    :param snake_body: Grupo con el cuerpo de la serpiente.
    :return:
    """
    body_size = len(snake_body.sprites()) - 1

    for i in range (body_size, 0, -1):
        snake_body.sprites()[i].rect.x =snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i - 1].rect.y

    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_collision(screen:pygame.surface.Surface, snake_body: pygame.sprite.Group, apples:pygame.sprite.Group, audio: Audio) -> bool:
    """
    Función que revisa las colisiones del juego.
    * Cabeza de la serpiente.
    * Cabeza de la serpiente con el borde de la pantalla.
    * Cabeza de la serpiente con la manzana.
    :param screen: Pantalla.
    :param snake_body: Cuerpo de la serpiente.
    :param apples: Grupo con las manzanas.
    :return: La bandera de fin de juego.
    """
    # Se declara la bandera de fin de juego.
    game_over = False

    # Se obtiene la cabeza de la serpiente.
    head = snake_body.sprites()[0]

    # Se revisa la condición de cabeza de la serpiente con el borde de la pantalla.
    screen_rect = screen.get_rect()

    if head.rect.right > screen_rect.right or head.rect.left < screen_rect.left or head.rect.top < screen_rect.top or head.rect.bottom > screen_rect.bottom:
        game_over = True

    # Se revisa la condición de cabeza de la serpiente con el cuerpo de la serpiente.
    head_body_collisions = pygame.sprite.spritecollide(head, snake_body, dokill=False)

    if len(head_body_collisions) > 1:
        game_over = True

    # Se revisa la condición de la cabeza de la serpiente con la manzana.
    head_apples_collisions = pygame.sprite.spritecollide(head, apples, dokill=True)

    if len(head_apples_collisions) > 0:
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple = Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

        audio.play_eats_apple_sound()

    return game_over

def screen_refresh(screen:pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group, apples:pygame.sprite.Group, background: Background) -> None:
    """
    Función que administra los elemento visuales del juego.
    :return:
    """
    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    # Fondo de Pantalla en formato RGB
    #screen.fill(Configurations.get_background())

    # Se anima el movimiento de la manzana.
    apples.sprites()[0].animate_apple()

    # Se dibuja la manzana
    apples.draw(screen)

    # Se dibuja el cuerpo de la serpiente.
    for snake_block in reversed(snake_body.sprites()):
        snake_body.sprites()[0].animate_head()
        snake_block.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego.
    clock.tick(Configurations.get_fps())

def game_over_screen(audio:Audio) -> None:
    """
    Función con la parte de fin de juego.
    """
    audio.music_fadeout(time = Configurations.get_music_fadeout_time())
    audio.play_game_over_sound()

    time.sleep(Configurations.get_game_over_screen_time())