import os
import pygame

sprites = {}

def loadSprite():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def getSprite(name):
    return sprites[name]