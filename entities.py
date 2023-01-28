import pygame
import pymunk

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img=pygame.image.load("img/boper.png").convert_alpha()
        self.img=pygame.transform.scale(self.img,(100,100))
        self.image = self.img
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("img/pig.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.image = self.img
        self.rect = self.image.get_rect()