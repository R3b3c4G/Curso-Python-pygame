"""
Nombre:
Fecha:

versión 0.5

"""

# Se importa los módulos del videojuego.
import pygame
from Configuration import Configurations
from Game_functionalities import game_events, screen_refresh, snake_movement
from Snake import SnakeBlock
from pygame.sprite import Group



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
    # Ciclo principal del juego.
    game_over = False

    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        game_over = game_events()

        snake_movement(snake_body)
        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen,clock, snake_body)

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()