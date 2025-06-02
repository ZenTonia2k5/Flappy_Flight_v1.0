import pygame

import assets
import configs
from objects.background import Background
from objects.column import Column
from objects.floor import Floor
from objects.plane import Plane
from objects.gameStartMessage import gameStartMessage
from objects.gameOverMessage import gameOverMessage
from objects.score import Score

pygame.init()

pygame.display.set_caption("Flappy Flight")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
columnTimer = pygame.USEREVENT
running = True
gameOver = False
gameStart = False

assets.loadSprite()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()

def createSprites():
    Background(0, sprites)
    Background(1, sprites)

    Floor(0, sprites)
    Floor(1, sprites)

    return Plane(sprites), gameStartMessage(sprites), Score(sprites)

plane, startMessage, score = createSprites()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == columnTimer:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gameStart and not gameOver:
                gameStart = True
                startMessage.kill()
                pygame.time.set_timer(columnTimer, 1500)

            if event.key == pygame.K_ESCAPE and gameOver:
                gameOver = False
                gameStart = False
                sprites.empty()
                plane, startMessage, score = createSprites()

        if not gameOver:
            plane.handleEvent(event)

    screen.fill(0)

    for sprite in sprites:
        if isinstance(sprite, Background):
            sprite.draw(screen)
        else:
            screen.blit(sprite.image, sprite.rect)

    if gameStart and not gameOver:
        sprites.update()

    if plane.checkCollision(sprites) and not gameOver:
        gameOver = True
        gameStart = False
        gameOverMessage(sprites)
        pygame.time.set_timer(columnTimer, 0)
        #assets.play_audio("hit")

    for sprite in sprites:
        if type(sprite) is Column and sprite.isPass():
            score.value += 1
            #assets.play_audio("point")

    pygame.display.flip()
    clock.tick(configs.FPS)
pygame.quit()