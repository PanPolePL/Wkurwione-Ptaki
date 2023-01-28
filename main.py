import sys
import pygame
import pymunk
import time
from entities import Player
from entities import Enemy
from ui import Arrow

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wkurwione Ptaki")
clock = pygame.time.Clock()
prev_time = time.time()
bg = 0, 0, 0

sprite_list = pygame.sprite.Group()

boper = Player()
boper.rect.x = 100
boper.rect.y = 500
sprite_list.add(boper)

pig = Enemy()
pig.rect.x = 1080
pig.rect.y = 500
sprite_list.add(pig)

aim = Arrow()
aim.rect.x = 100
aim.rect.y = 550

mouse_pressed=False
mouse_x=0
mouse_y=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        if mouse_pressed:
            sprite_list.add(aim)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)

        else:
            sprite_list.remove(aim)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    clock.tick(75)
    screen.fill(bg)
    sprite_list.draw(screen)
    pygame.display.flip()
