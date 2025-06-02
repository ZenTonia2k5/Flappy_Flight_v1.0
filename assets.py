import os
import pygame

sprites = {}
audios = {}

def loadSprite():
    path = os.path.join("assets", "sprites")
    valid_extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]  # supported image formats

    for file in os.listdir(path):
        if any(file.lower().endswith(ext) for ext in valid_extensions):
            sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def load_audios():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def getSprite(name):
    return sprites[name]

def play_audio(name):
    audios[name].play()