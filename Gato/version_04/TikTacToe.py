import pygame.image
from pygame.sprite import Sprite
from Configurations import Configurations


class TicTacToeMark(Sprite):
    _turno = "X"
    def __init__(self, cell_number):
        """
        Constructor de la clase que representan las marcas X y O.
        """
        super().__init__()
        if self._turno == "X":
            self.image = pygame.image.load(Configurations.get_markX_image_path())
        else:
            self.image = pygame.image.load(Configurations.get_markO_image_path())

        # Escalar imagen marca.
        self.image = pygame.transform.scale(self.image,Configurations.get_mark_size())

        # Posicionar imagen marca.
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Configurations.get_cell_positions(cell_number)

        # Cambiar turno.
        if self._turno == "X":
            TicTacToeMark._turno = "O"
        else:
            TicTacToeMark._turno = "X"


    @classmethod
    def get_turno(cls)-> str:
        """
        Getter para _turno.
        :return:
        """
        return cls._turno