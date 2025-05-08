"""
Nombre:
Fecha:
Versión 0.1:
"""

# Se importa los módulos del videojuego.
import pygame

def run_game() -> None:
    """
    Función principal de videojuego.
    """

    # Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen_size = (780, 500)   # Resolución de pantalla(ancho, alto)
    screen = pygame.display.set_mode(screen_size)   # Va ser un objeto(tupla)/ Pantalla fija

    # Se configura el título dle juego.
    game_title = "Snake game en pygame"
    pygame.display.set_caption(game_title)

    # Ciclo principal del juego.
    game_over = False

    while not game_over:
        # Se verifica los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            # Un clic en cerrar el juego.
            if event.type == pygame.QUIT:   # Evento cerrar ventana.
                game_over = True

            # Se dibujan los elementos gráficos en la pantalla
            background = (50, 230, 50)  # Fondo de la pantalla en
            screen.fill(background)

            # Se actualiza la pantalla.
            pygame.display.flip()

    # Se cierran los recursos
    pygame.quit()

if __name__=="__main__":
    run_game()