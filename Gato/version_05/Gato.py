"""
Fecha: 19 de mayo de 2025.
Equipo: Duo binario.
Integrantes: Héctor Jesús Méndez Santiago, Rebeca Gregorio Espina.

Archivo donde se reproducirá el juego principal del gato.
Versión 0.5:
Ahora se verifica que las casillas no estén ocupadas al crear una nueva marca.


"""

# Se importa los módulos del videojuego.
import pygame
from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh
from Media import Background, TurnImage

def run_game() -> None:
    """
    Función principal de videojuego del gato.

    """
    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se configura el reloj del juego.
    clock = pygame.time.Clock()

    # Se inicializa la pantalla.
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el título dle juego.
    pygame.display.set_caption(Configurations.get_game_title())

    # Se crea el objeto con el fondo de pantalla.
    background = Background()

    # Grupo de las marcas.
    marks_group = pygame.sprite.Group()

    # Imagen del turno.
    turn_image = TurnImage()

    # Ciclo principal del juego.
    game_over = False
    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        game_over = game_events(marks_group, turn_image)

        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background, marks_group, turn_image)

        # Se actualiza la pantalla.
        pygame.display.flip()

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()