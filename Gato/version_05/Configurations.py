class Configurations:
    """
    Clase que contiene todas las configuraciones del juego del gato.
    """
    # Configuraciones de la pantalla.
    _screen_size = (780, 680)               # Resolución de pantalla(ancho, alto)
    _game_title = "Snake game en pygame"    # Título de juego.
    _background = (0, 0, 0)                 # Fondo de la pantalla en formato RGB.
    _fps = 8                                # Fotogramas por segundo.

    # Rutas de archivos multimedia.
    _background_image_path = "../media/background_image.png"
    _markO_image_path = "../media/markO.png"
    _markX_image_path = "../media/markX.png"
    _turnO_image_path = "../media/turnO.png"
    _turnX_image_path = "../media/turnX.png"

    _mark_size = (65,65)
    _cell_positions ={
        1:(274,274), 2:(357,274), 3:(440,274),
        4:(274,392), 5:(357,392), 6:(440,392),
        7:(274, 504), 8:(357, 504), 9:(440, 504)
    }

    _size_turn_image = (300, 200)
    _turn_image_position = (5,20)

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """
        Getter para _background.
        """
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path
        """
        return cls._background_image_path

    @classmethod
    def get_markO_image_path(cls) -> str:
        """
        Getter para _markO_image_path
        """
        return cls._markO_image_path

    @classmethod
    def get_markX_image_path(cls) -> str:
        """
        Getter para _markX_image_path
        """
        return cls._markX_image_path

    @classmethod
    def get_turnO_image_path(cls) -> str:
        """
        Getter para _turnO_image_path
        """
        return cls._turnO_image_path

    @classmethod
    def get_turnX_image_path(cls) -> str:
        """
        Getter para _turnX_image_path
        """
        return cls._turnX_image_path

    @classmethod
    def get_mark_size(cls) -> tuple[int,int]:
        """
        Getter para _mark_size
        """
        return cls._mark_size

    @classmethod
    def get_cell_positions(cls, cell_number:int) -> tuple[int, int] | None:
        """
        Getter para _cell_positions
        """
        if cell_number in cls._cell_positions:
            return cls._cell_positions[cell_number]
        return None

    @classmethod
    def get_size_turn_image(cls) -> int:
        """
        Getter para tamaño de imagen de los turnos
        """
        return cls._size_turn_image

    @classmethod
    def get_turn_image_position(cls) -> tuple[int,int]:
        """
        Getter para _turn_image_position
        """
        return cls._turn_image_position
