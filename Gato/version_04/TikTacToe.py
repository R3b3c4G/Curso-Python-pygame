from pygame.sprite import Sprite

from Configurations import Configurations


class TicTacToeMark(Sprite):
    turno = "X"
    def __init__(self, box_number):
        """
        Constructor de la clase que representan las marcas X y O.
        """
        super().__init__()
        if TicTacToeMark.turno == "X":
            image_path = Configurations.get_markX_image_path()
        else:
            image_path = Configurations.get_markO_image_path()
