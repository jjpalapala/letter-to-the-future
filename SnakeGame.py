import pygame
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(3,12),Vector2(4,12),Vector2(5,12)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x_position = int(block.x * CELL_SIZE)
            y_position = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_position,y_position,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,RED,block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,CELL_NUMBER - 1)
        self.y = random.randint(0,CELL_NUMBER - 1)
        self.position = Vector2(self.x,self.y)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * CELL_SIZE),int(self.position.y* CELL_SIZE),CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen,(0,255,255),fruit_rect)
#2
pygame.init()

CELL_SIZE= 25
CELL_NUMBER = 25
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER,CELL_NUMBER*CELL_SIZE))
pygame.display.set_caption("SuperSnake")
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            Running = False
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            elif event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)

    screen.fill(GREEN)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
