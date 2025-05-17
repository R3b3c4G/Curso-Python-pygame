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
    Clase que contiene la imagen de turno.
    """
    def __init__(self):
        self.image = pygame.image.load(Configurations.get_turnX_image_path())
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Configurations.get_turn_image_position()

    def change_turn(self, turn: str) -> None:
        """
        Se usa para conmutar la imagen del turno.
        :param turn: Turno actual.
        """
        if turn == "X":
            self.image = pygame.image.load(Configurations.get_turnX_image_path())
        else:
            self.image = pygame.image.load(Configurations.get_turnO_image_path())
        self.image = pygame.transform.scale(self.image, Configurations.get_size_turn_image())

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Configurations.get_turn_image_position()
