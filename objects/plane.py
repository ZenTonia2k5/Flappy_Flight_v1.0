import pygame.sprite

import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor


class Plane(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER

        self.images = [
            assets.getSprite("plane")
            #assets.getSprite("_") if need more animation
        ]

        self.flap = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (100, 280))
        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)

    def update(self):
        self.images.insert( 0, self.images.pop())
        self.image = self.images[0]

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 1

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #assets.play_audio("")
            self.flap = 0
            self.flap -= 5

    def checkCollision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(self.mask, (
                    self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or self.rect.bottom < 0):
                return True
        return False