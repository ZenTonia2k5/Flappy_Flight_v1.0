import pygame.sprite

import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.BACKGROUND

        self.image = assets.getSprite("bg")
        self.rect = self.image.get_rect(topleft = (configs.SCREEN_WIDTH * index, 0))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1
        if self.rect.x <= -self.rect.width:
            self.rect.x = 0  # Reset to show the entire bg again

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, 0))
        # Draw the second copy next to the first to fill the gap
        surface.blit(self.image, (self.rect.x + self.rect.width, 0))