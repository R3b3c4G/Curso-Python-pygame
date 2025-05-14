"""
Fecha: 19 de mayo de 2025.
Equipo: Duo binario.
Integrantes: Héctor Jesús Méndez Santiago, Rebeca Gregorio Espina.

Archivo donde se reproducirá el juego principal del gato.
Versión 0.2:
Se agregó la clase Configurations en el módulo Configurations.py (nuevo).
Esta clase va a incluir todas las configuraciones del juego.

Se agregó el módulo Game_functionalities.py (nuevo).
Este módulo va a contener todas las funcionalidades del juego.

En esta versión, contiene las funciones que administran los eventos del juego, llamada game_events(), y los elementos de la pantalla, llamada screen_refresh().
La función game_events() retorna la bandera del fin del juego.
La función screen_refresh() recibe el objeto con la pantalla.
Se refactorizó el código de la versión anterior para reflejar los cambios anteriores.
"""

# Se importa los módulos del videojuego.
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh

def run_game() -> None:
    """
    Función principal de videojuego del gato.
    """

    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el título dle juego.
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del juego.
    game_over = False
    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        game_over = game_events()

        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen)

        # Se actualiza la pantalla.
        pygame.display.flip()

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()