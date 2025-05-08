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
    _time_to_refresh_head_frames = 1000

    # Configuraciones de la manzana.
    _apple_block_size =_snake_block_size    # Color de la manzana.
    _apple_color = (255, 0, 0)
    _time_to_refresh_apple_frames= 1000

    # Rutas de los archivos multimedia
    _background_image_path = "../media/background_image.jpg"
    _apple_images_path = ["../media/apple1.png", "../media/apple2.png","../media/apple3.png","../media/apple4.png"]
    _head_images_path = ["../media/head1.png", "../media/head2.png", "../media/head3.png", "../media/head4.png",
                         "../media/head5.png" ,"../media/head6.png", "../media/head7.png", "../media/head8.png"]

    _snake_head_image_path = "../media/head1.png"
    _snake_body_image_path = ["../media/body1.png", "../media/body2.png", "../media/body3.png"]

    # Configuraciones de la música del juego.
    _music_volume = 0.25
    _music_fadeout_time = _game_over_screen_time

    # Rutas de los audios utilizados en la clase audio
    _music_path = "../media/music.mp3"
    _start_sounds_path = "../media/start_sound.wav"
    _eats_apple_sound_path= "../media/eats_apple_sound.wav"
    _game_over_sound_path = "../media/game_over_sound.wav"


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

    @classmethod
    def get_time_to_refresh_head_frames(cls) -> int:
        return cls._time_to_refresh_head_frames

    @classmethod
    def get_head_images_path(cls) -> list:
        return cls._head_images_path

    @classmethod
    def get_music_volume(cls) -> float:
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        return cls._music_path

    @classmethod
    def get_start_sounds_path(cls) -> str:
        return cls._start_sounds_path

    @classmethod
    def get_eats_apple_sound_path(cls) -> str:
        return cls._eats_apple_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        return cls._game_over_sound_path


