import pygame
from Configuration import Configurations

class Background:
    """
    Clase   que contiene el fonco de pantalla.
    """
    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen:pygame.surface.Surface):
        """Se utiliza para dibujar el fondo de pantalla"""
        screen.blit(self.image, self.rect)
