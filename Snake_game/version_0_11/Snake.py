from random import randint, choice
import pygame
from pygame.sprite import Sprite
from Configuration import Configurations

# Concepto de herencia
class SnakeBlock(Sprite):
    # Atributos de clase (banderas de movimiento de la serpiente).
    _is_moving_right = False
    _is_moving_left = False
    _is_moving_up = False
    _is_moving_down = False
    def __init__(self, is_head: bool = False):
        """
        Constructor de la clase.
        """
        super().__init__()
        if is_head:
            #color = Configurations.get_snake_head_color()
            #self.image = pygame.image.load(Configurations.get_snake_head_image_path())
            self._snake_head_frames = []

            snake_head_block_size = Configurations.get_snake_block_size()

            for i in range(len(Configurations.get_head_images_path())):
                frame = pygame.image.load(Configurations.get_head_images_path()[i])
                frame = pygame.transform.scale(frame, (snake_head_block_size, snake_head_block_size))
                self._snake_head_frames.append(frame)

            self._last_update_time = pygame.time.get_ticks()

            self._frame_index = 0

            # self.image = pygame.image.load(Configurations.get_apple_image_path()[0])
            # self.image = pygame.transform.scale(self.image,(apple_block_size,apple_block_size))

            self.image = self._snake_head_frames[self._frame_index]
            self._frame_index = 1

        else:
            #color = Configurations.get_snake_body_color()
            body_images_path = Configurations.get_snake_body_image_path()
            path = choice(body_images_path)

            self.image = pygame.image.load(path)

        snake_block_size = Configurations.get_snake_block_size()
        #self.image = pygame.Surface((snake_block_size, snake_block_size))
        #self.image.fill(color)
        self.image = pygame.transform.scale(self.image,(snake_block_size,snake_block_size))

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente.
        :param screen:  Pantalla en donde se dibuja.
        :return:
        """
        angle = 0

        if SnakeBlock.get_is_moving_up():
            angle = 90

        elif SnakeBlock.get_is_moving_left():
            angle = 180

        elif SnakeBlock.get_is_moving_down():
            angle = 270

        image_flip = pygame.transform.rotate(self.image,angle)
        screen.blit(image_flip, self.rect)

    def snake_head_init(self) -> None:
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()

        # Posicionar aleatoriamente la cabeza de la serpiente.
        self.rect.x = snake_block_size * randint(0, (screen_width //  snake_block_size)-1)
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size)-1)

    @classmethod
    def get_is_moving_right(cls) -> bool:
        """
        Getter para la bandera _is_moving_right
        :return:
        """
        return cls._is_moving_right

    @classmethod
    def set_is_moving_right(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_right
        :return:
        """
        cls._is_moving_right = value

    @classmethod
    def get_is_moving_left(cls) -> bool:
        """
        Getter para la bandera _is_moving_left
        :return:
        """
        return cls._is_moving_left

    @classmethod
    def set_is_moving_left(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_left
        :return:
        """
        cls._is_moving_left = value

    @classmethod
    def get_is_moving_up(cls) -> bool:
        """
        Getter para la bandera _is_moving_up
        :return:
        """
        return cls._is_moving_up

    @classmethod
    def set_is_moving_up(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_up
        :return:
        """
        cls._is_moving_up = value


    @classmethod
    def get_is_moving_down(cls) -> bool:
        """
        Getter para la bandera _is_moving_up
        :return:
        """
        return cls._is_moving_down

    @classmethod
    def set_is_moving_down(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_down
        :return:
        """
        cls._is_moving_down = value

    def animate_head(self) -> None:
        """
        Se utiliza para actualizar el frame visible de la cabeza, dando la impresión de movimiento.
        """
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh_head_frames()

        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._snake_head_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._snake_head_frames):
                self._frame_index = 0

