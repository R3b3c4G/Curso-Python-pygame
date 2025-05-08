"""
Nombre:
Fecha:

versión 0.2
- Se agregó la clase Configutations el módulo Configurations.py que va a incluir todas las configuracion del juego.
"""

# Se importa los módulos del videojuego.
import pygame
from Configuration import Configurations
from Game_functionalities import game_events, screen_refresh

def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    # screen_size = (1280, 720)   # Resolución de pantalla(ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size())   # Va ser un objeto(tupla)/ Pantalla fija

    # Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del juego.
    game_over = False

    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        game_over = game_events()

        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen)

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()