import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_background_image_path())
        self.image = pygame.transform.scale(self.image, Configurations.get_screen_size())
        self.rect = self.image.get_rect()

    def blit(self, screen:pygame.surface.Surface):
        """
        Función utilizada para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)

class TurnImage:
    """
    Clase que contiene el turno del juego.
    """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_turnX_image_path())
        image_size = Configurations.get_size_turn_image()
        self.image = pygame.transform.scale(self.image, image_size)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Configurations.get_turn_image_position()

    def change_turn(self, turn: str) -> None:
        """
        Se usa para conmutar la imagen del turno.
        :param turn: Turno actual.
        """
        if turn == "X":
            self.image = pygame.image.load(Configurations.get_turnX_image_path())
            self.image = pygame.transform.scale(self.image, Configurations.get_size_turn_image())
        else:
            self.image = pygame.image.load(Configurations.get_turnO_image_path())
            self.image = pygame.transform.scale(self.image, Configurations.get_size_turn_image())

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Configurations.get_turn_image_position()

    def blit(self, screen):
        screen.blit(self.image, self.rect)


class ResultsImage:
    """
    Clase que contiene la pantalla del fin del juego.
    """
    def __init__(self, result: str):
        if result == "X":
            self.image = pygame.image.load(Configurations.get_winX_image_path())
        elif result == "O":
            self.image = pygame.image.load(Configurations.get_winO_image_path())
        else:  # Empate
            self.image = pygame.image.load(Configurations.get_draw_image_path())

        self.image = pygame.transform.scale(self.image, Configurations.get_image_size_results())
        self.rect = self.image.get_rect()
        screen_size = Configurations.get_screen_size()
        self.rect.centerx = screen_size[0] // 2  # Ancho.
        self.rect.y = 50  # 50px desde arriba


class CreditsImage:
    """
    Clase que muestra los créditos del juego.
    """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_credits_image_path())
        self.image = pygame.transform.scale(self.image, Configurations.get_image_size_credits())
        self.rect = self.image.get_rect()
        screen_size = Configurations.get_screen_size()
        self.rect.centerx = screen_size[0] // 2 # Ancho.  # La mitad del ancho de pantalla
        self.rect.bottom = screen_size[1] - 20  #Alto # 20px desde abajo

    def blit(self, screen):
        screen.blit(self.image, self.rect)