class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (780, 680)               # Resolución de pantalla(ancho, alto)
    _game_title = "Snake game en pygame"    # Título de juego.
    _background = (50, 230, 50)             # Fondo de la pantalla en formato RGB.

    @classmethod    # Método para clase
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size


    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int]:
        """
        Getter para _background.
        """
        return cls._background