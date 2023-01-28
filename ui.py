import pygame
import pymunk

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("img/arrow.png")
        self.img = pygame.transform.scale(self.img, (200, 40))
        self.image = self.img
        self.rect = self.image.get_rect()