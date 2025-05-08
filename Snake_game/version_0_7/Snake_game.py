"""
Nombre:
Fecha:

versión 0.6
- Se agrega bloques al cuerpo de la serpiente.
"""

# Se importa los módulos del videojuego.
import pygame
from Configuration import Configurations
from Game_functionalities import game_events, screen_refresh, snake_movement
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple



def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se configura el reloj del juego.
    clock = pygame.time.Clock()

    # Se inicializa la pantalla.
    screen = pygame.display.set_mode(Configurations.get_screen_size())   # Va ser un objeto(tupla)/ Pantalla fija

    # Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())

    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()

    # Se crea el grupo para almacenar el cuerpo de la serpiente.
    snake_body = Group()
    snake_body.add(snake_head)

    # se crea el bloque inicial de las manzanas.
    apple = Apple()
    apple.random_position(snake_body)

    # Se crea un grupo con las manzanas.
    apples = Group()
    apples.add(apple)


    # Ciclo principal del juego.
    game_over = False

    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        game_over = game_events(snake_body, apples)
    # Se administra el movimiento
        snake_movement(snake_body)
        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen,clock, snake_body, apples)

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()