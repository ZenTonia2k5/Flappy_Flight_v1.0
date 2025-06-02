import random

import pygame.sprite

import assets
import configs
from layer import Layer


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.OBSTACLE
        self.gap = 100

        self.sprite = assets.getSprite("tower")
        self.sprite_rect = self.sprite.get_rect()

        self.towerBottom = self.sprite
        self.towerBottom_rect = self.towerBottom.get_rect(topleft=(0, self.sprite_rect.height + self.gap))

        self.towerTop = pygame.transform.flip(self.sprite, False, True)
        self.towerTop_rect = self.towerTop.get_rect(topleft = (0, 0))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap),
                                            pygame.SRCALPHA)
        self.image.blit(self.towerBottom, self.towerBottom_rect)
        self.image.blit(self.towerTop, self.towerTop_rect)

        sprites_floor_height = assets.getSprite("roadFloor").get_rect().height
        min_y = 100
        max_y = configs.SCREEN_HEIGHT - sprites_floor_height - 100

        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))
        self.mask = pygame.mask.from_surface(self.image)

        self.passed = False

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.kill()

    def isPass(self):
        if self.rect.x < 40 and not self.passed:
            self.passed = True
            return True
        return False