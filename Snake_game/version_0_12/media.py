import pygame
from Configuration import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.

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

class Audio:
    def __init__(self):
        # Se carga la música del juego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se cargan los sonidos.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sounds_path())
        self._eats_apple_sound = pygame.mixer.Sound(Configurations.get_eats_apple_sound_path())
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

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

    def play_start_sound(self) -> None:
        self._start_sound.play()

    def play_eats_apple_sound(self) -> None:
        self._eats_apple_sound.play()

    def play_game_over_sound(self) -> None:
        self._game_over_sound.play()

class Scoreboard:
    def __init__(self):
        self._typeface = "Kimono"
        self._font_size = 40
        self._font_color = (171, 250,10)

        # Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("Puntos: 0", True, self._font_color)
        self.rect = self.image.get_rect()

        # Se ajusta la posición del marcador
        self.rect.x = int(Configurations.get_screen_size()[0] * 0.05)
        self.rect.y = int(Configurations.get_screen_size()[1] * 0.05)

    def update(self, new_score:int) -> None:
        text = "Puntos: "+ str(new_score)
        self.image = self._font.render(text, True, self._font_color)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)

class GameOverImage:
    def __init__(self):
        self.image = pygame.image.load("../media/game_over_image.png")
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom-Configurations.get_snake_block_size()
        screen.blit(self.image,self.rect)
