import pygame

import assets
import configs
from layer import Layer


class gameStartMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI

        self.image = assets.getSprite("start")
        self.rect = self.image.get_rect(center = (configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))

        super().__init__(*groups)