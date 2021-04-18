import pygame
import random
import os
import shutil
pygame.init()
# =============================================
# Window parameters
# =============================================
winWidth = 640
winHeight = 640
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface((winWidth, winHeight))  # width,height
bg.fill((0, 0, 0))  # color
pygame.display.set_caption("Snake")

# =============================================
# Parent Class
# =============================================


class GameObject(object):
    def __init__(self, x=10, y=10, color=(255, 255, 255), speed=8):
        self.x = x
        self.y = y
        self.color = color

# =============================================
# Wall Class
# =============================================


class Wall(GameObject):
    def __init__(self, x=0, y=0, color=(255, 255, 255), width=32, height=32):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height), 3)
        # hitbox draw
        # self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(
        #     win, [0, 255, 0], (self.x, self.y, self.width, self.height), 1)


# =============================================
# Fruit Class
# =============================================


class Fruit(GameObject):
    def __init__(self, x=-200, y=-200, color=(255, 255, 255), width=16, height=16):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        # hitbox draw
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(
            win, [0, 255, 0], (self.x, self.y, self.width, self.height), 1)
# =============================================
# Snake Class
# =============================================


class Snake(object):
    def __init__(self):
        self.x = 128
        self.y = 128
        self.speed = 8
        self.velocity = [self.speed, 0]  # dx,dy
        self.size = 1
        self.radius = 8
        self.hitbox = pygame.Rect(
            self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.elements = [[self.x, self.y, self.hitbox]]
        self.up = False
        self.down = False
        self.right = True
        self.left = False
        for i in range(10):
            self.add_size()

    def add_size(self):
        self.size += 1
        self.hitbox = pygame.Rect(
            self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.elements.append([self.x, self.y, self.hitbox])

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(
                win, ((3*element[0]) % 256, 100, (element[0]+element[1]) % 256), element[0:2], self.radius)
            self.hitbox = pygame.Rect(
                element[0]-self.radius, element[1]-self.radius, self.radius*2, self.radius*2)
            ind = self.elements.index(element)
            self.elements[ind][2] = self.hitbox

            pygame.draw.rect(
                win, [0, 255, 0], (element[0]-self.radius, element[1]-self.radius, self.radius*2, self.radius*2), 1)

    def move(self):
        for i in range(1, self.size):
            self.elements[self.size-i][0] = self.elements[self.size-i-1][0]
            self.elements[self.size-i][1] = self.elements[self.size-i-1][1]
        self.elements[0][0] += self.velocity[0]
        self.elements[0][1] += self.velocity[1]


# =============================================
# Functions
# =============================================
def draw_score():
    global score
    font = pygame.font.SysFont('ComicSans', 24)
    text = font.render(f'Score:{score}', 1, (255, 255, 255))
    win.blit(text, (500, 50))


def spawn_fruit():
    while len(fruits) < 5:
        # def __init__(self, x=0, y=0, color=(255, 255, 255), width=16, height=16):
        x_ = random.randrange(64, 600, 32)
        y_ = random.randrange(64, 600, 32)
        color_ = (random.randrange(100, 255), random.randrange(
            100, 255), random.randrange(100, 255))
        width_ = height_ = random.randrange(8, 24, 4)
        fruits.append(Fruit(x_, y_, color_, width_, height_))


def display_update():
    global score
    win.blit(bg, (0, 0))
    draw_score()
    for wall in walls:
        wall.draw()
    for fruit in fruits:
        fruit.draw()
    snake.draw()
    snake.move()
    for fruit in fruits:
        if snake.elements[0][2].colliderect(fruit.hitbox):
            score += 1
            snake.add_size()
            fruits.remove(fruit)
    pygame.display.update()


def create_map(level_num):
    with open(f'games/Snake/maps/map{level_num}', mode='r') as file:
        row_num = 0  # row number
        for row in file:
            for block_num in range(len(row)):
                if row[block_num] == '1':
                    walls.append(Wall(row_num*32, block_num*32,
                                      ((16*row_num) % 256, (16*block_num) % 256, 200)))
            row_num += 1

# =============================================
# Variables
# =============================================


FPS = 16
run = True
clock = pygame.time.Clock()


level_num = 1
score = 0
walls = []
fruits = []
snake = Snake()
# =============================================
# Main function
# =============================================


def start_game():
    global run
    create_map(level_num)
    while run:
        ms = clock.tick(FPS)  # FPS - fps, ms - millsec between frames
        display_update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_d] and not snake.left:
            snake.right = True
            snake.up = snake.down = snake.left = False
            snake.velocity = [snake.speed, 0]
        elif keys[pygame.K_a] and not snake.right:
            snake.left = True
            snake.up = snake.down = snake.right = False
            snake.velocity = [-snake.speed, 0]
        elif keys[pygame.K_w] and not snake.down:
            snake.up = True
            snake.down = snake.right = snake.left = False
            snake.velocity = [0, -snake.speed]
        elif keys[pygame.K_s] and not snake.up:
            snake.down = True
            snake.up = snake.right = snake.left = False
            snake.velocity = [0, snake.speed]
        spawn_fruit()


start_game()
pygame.quit()
