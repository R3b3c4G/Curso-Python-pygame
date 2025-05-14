"""
Fecha: 19 de mayo de 2025.
Equipo: Duo binario.
Integrantes: Héctor Jesús Méndez Santiago, Rebeca Gregorio Espina.

Archivo donde se reproducirá el juego principal del gato.
Versión 0.1:
Se muestra una pantalla con un fondo de un solo color y el título de la ventana "Juego del gato" y el
único evento que se maneja es cerrar la ventana.
"""

# Se importa los módulos del videojuego.
import pygame

def run_game() -> None:
    """
    Función principal de videojuego del gato.
    """

    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen_size = (780, 500)   # Resolución de pantalla(ancho, alto)
    screen = pygame.display.set_mode(screen_size)   # Va ser un objeto(tupla)/ Pantalla fija

    # Se configura el título del juego.
    game_title = "Juego del gato"
    pygame.display.set_caption(game_title)

    # Ciclo principal del juego.
    game_over = False

    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            # Un clic en cerrar el juego.
            if event.type == pygame.QUIT:   # Evento cerrar ventana.
                game_over = True

            # Se dibujan los elementos gráficos en la pantalla.
            background = (0,0,0)  # Fondo de la pantalla en un sólo color.
            screen.fill(background)

            # Se actualiza la pantalla.
            pygame.display.flip()

    # Se cierran los recursos.
    pygame.quit()

if __name__=="__main__":
    run_game()