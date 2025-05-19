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
        else:
            self.image = pygame.image.load(Configurations.get_turnO_image_path())

        # Reescalar y reposicionar la misma imagen.
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
        self.rect.y = 250  # 250px desde arriba


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

class Audio:
    """
    Clase que contiene los sonidos y música del juego.
    """
    def __init__(self):
        # Se carga la música del juego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se cargan los efectos de sonido.
        self._cat_keyboard_sound = pygame.mixer.Sound(Configurations.get_keyboard_sound_path())
        self._cat_results_sound = pygame.mixer.Sound(Configurations.get_results_sound_path())

    @classmethod
    def play_music(cls, volume) -> None:
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Time de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def play_cat_keyboard_sound(self) -> None:
        self._cat_keyboard_sound.play()

    def play_result_sound(self) -> None:
        self._cat_results_sound.play()
