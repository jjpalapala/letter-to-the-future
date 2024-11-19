import pygame
import random

pygame.init()

HEIGHT = 625
WIDTH = 625
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SuperSnake")
screen.fill(WHITE)
clock = pygame.time.Clock()

FPS = 15
x = HEIGHT // 2
y = WIDTH // 2
speed_snake = 25
x_change = 0
y_change = 0

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            Running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed_snake
                x_change = 0
            elif event.key == pygame.K_RIGHT:
                x += speed_snake
                x_change = 0
            elif event.key == pygame.K_UP:
                y -= speed_snake
                y_change = 0
            elif event.key == pygame.K_DOWN:
                y += speed_snake
                y_change = 0

    pygame.draw.rect(screen, GREEN,[x,y,25,25])
    pygame.display.update()
    clock.tick(FPS)
