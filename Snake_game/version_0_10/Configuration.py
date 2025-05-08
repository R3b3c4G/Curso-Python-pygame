class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (760, 680)               # Resolución de pantalla(ancho, alto)/ Se modificó para que se ajustara al tamaño de bloques.
    _game_title = "Snake game en pygame"    # Título de juego.
    #_background = (50, 230, 50)             # Fondo de la pantalla en formato RGB.
    _fps = 8                                # FPS del juego (velocidad)
    _game_over_screen_time = 4
    # Configuraciones de la serpiente.
    _snake_block_size = 40      # Tamaño de bloque de la serpiente.
    _snake_head_color = (255, 255, 255) # Color de la cabeza de la serpiente.
    _snake_body_color = (0, 255, 0)

    # Configuraciones de la manzana.
    _apple_block_size =_snake_block_size    # Color de la manzana.
    _apple_color = (255, 0, 0)
    _time_to_refresh_apple_frames= 1000

    # Rutas de los archivos multimedia
    _background_image_path = "../media/background_image.jpg"
    _apple_images_path = ["../media/apple1.png", "../media/apple2.png","../media/apple3.png","../media/apple4.png"]

    _snake_head_image_path = "../media/head1.png"
    _snake_body_image_path = ["../media/body1.png", "../media/body2.png", "../media/body3.png"]




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
        :return:
        """
        return cls._game_title

    #@classmethod
    #def get_background(cls) -> tuple[int, int, int]:
      #  """
     #   Getter para _background.
    #    """
     #   return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        """
        return cls._fps

    @classmethod
    def get_snake_block_size(cls) -> int:
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int,int]:
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int,int]:
        return cls._snake_body_color

    #@classmethod
    #def get_apple_color(cls) -> tuple[int, int,int]:
     #   return cls._apple_color

    @classmethod
    def get_apple_block_size(cls) -> int:
        return cls._apple_block_size

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        return cls._game_over_screen_time

    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path

    @classmethod
    def get_apple_images_path(cls) -> list:
        return cls._apple_images_path

    @classmethod
    def get_snake_head_image_path(cls) -> str:
        return cls._snake_head_image_path

    @classmethod
    def get_snake_body_image_path(cls) -> list:
        return cls._snake_body_image_path

    @classmethod
    def get_time_to_refresh_apple_frames(cls) -> int:
        return cls._time_to_refresh_apple_frames



