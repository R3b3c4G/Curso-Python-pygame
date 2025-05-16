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
