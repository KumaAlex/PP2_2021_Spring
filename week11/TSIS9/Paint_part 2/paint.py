import pygame
import json
import random

#===========================================================
# дано

width = 1000
height = 700

RED = (255, 0 ,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (123, 127, 127)
CYAN = (0, 255, 255)

pygame.init()
pygame.display.set_caption("Paint by ALEX")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 18)

pressed = False
pen_bool = True
cir_bool = False
rect_bool = False
startPos = (0, 0)
endPos = (0, 0)
done = False
colors = []
length = []

class Items:
    def __init__(self, name, x, y, color, x_size, y_size):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.x_size = x_size
        self.y_size = y_size
        self.hitbox = pygame.Rect(self.x, self.y, self.x_size, self.y_size)
    def draw_color(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_size, self.y_size))
    def draw_length(self):
        pygame.draw.circle(screen, BLACK, (self.x+20, self.y+20), self.color)
    def draw_hitbox(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.x_size, self.y_size))

colors.append(Items("BLACK", 20, 20, BLACK, 80, 80))
colors.append(Items("WHITE", 20, 100, WHITE, 80, 80))
colors.append(Items("BLUE", 100, 20, BLUE, 80, 80))
colors.append(Items("RED", 20, 260, RED, 80, 80))
colors.append(Items("GREEN", 100, 100, GREEN, 80, 80))
colors.append(Items("GREY", 100, 340, GREY, 80, 80))
colors.append(Items("PURPLE", 20, 180, PURPLE, 80, 80))
colors.append(Items("CYAN", 20, 340, CYAN, 80, 80))
colors.append(Items("YELLOW", 100, 180, YELLOW, 80, 80))
colors.append(Items("ORANGE", 100, 260, ORANGE, 80, 80))
eraser = Items("ERASER", 20, height-100, WHITE, 80, 80)
length.append(Items("L1", 20, 430, 3, 40, 40))
length.append(Items("L1", 60, 430, 6, 40, 40))
length.append(Items("L1", 100, 430, 10, 40, 40))
length.append(Items("L1", 140, 430, 20, 40, 40))
rect = Items("RECTANGLE", 100, height-180, WHITE, 80, 80)
cir = Items("CIRCLE", 20, height-180, WHITE, 80, 80)
pen = Items("PEN", 20, 480, BLACK, 160, 30)
save = Items("SAVE", 100, height-100, BLACK, 80, 80)

curColor = BLACK
curLenght = 3
screen.fill(WHITE)

def bg():
    pygame.draw.rect(screen, (179, 143, 251), (0, 0, 200, 700))


    pygame.draw.circle(screen, BLACK, (60, height - 140), 35, 3)
    pygame.draw.rect(screen, BLACK, (105, height - 175, 70, 70), 3)
    screen.blit(font.render("ERASE", 1, BLACK), (30, height-85))
    screen.blit(font.render("ALL", 1, BLACK), (45, height-65))
    screen.blit(font.render("SAVE", 1, BLACK), (115, height-80))
    screen.blit(font.render("STANDARD PEN", 1, BLACK), (30, height-220))

    for color in colors:
        color.draw_color()
    for size in length:
        size.draw_length()
    pygame.draw.line(screen, BLACK, (200, 0), (200, 700))
    pygame.draw.rect(screen, BLACK, (10, 10, 180, 680), 2)
    for i in range(3):
        pygame.draw.line(screen, BLACK, (20 + 80*i, 20), (20 + 80*i, 420), 3)
        pygame.draw.line(screen, BLACK, (20 + 80*i, height-20), (20 + 80*i, height-180), 3)
        pygame.draw.line(screen, BLACK, (20, height - 20 - 80*i), (180, height - 20 - 80*i), 3)
    for i in range(6):
        pygame.draw.line(screen, BLACK, (20, 20 + 80*i), (180, 20 + 80*i), 3)
    for i in range(4):
       pygame.draw.rect(screen, BLACK, (20 + 40*i, 430, 40, 40), 3)
    pygame.draw.rect(screen, BLACK, (20, 480, 160, 30), 3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        if pen_bool:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                startPos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
                endPos = pygame.mouse.get_pos()
                for col in colors:
                    if col.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curColor = col.color
                if eraser.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    screen.fill(WHITE)
                for size in length:
                    if size.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curLenght = size.color*2
                if cir.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = False
                    cir_bool = True
                if rect.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = True
                    cir_bool = False
                if pen.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = True
                    rect_bool = False
                    cir_bool = False
                if save.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pygame.image.save(screen, r"C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Paint_part 2\saved_image.png")
            elif event.type == pygame.MOUSEMOTION and pressed == True:
                x, y = pygame.mouse.get_pos()
                pygame.draw.line(screen, curColor, startPos, (x, y), curLenght)
                pygame.draw.circle(screen, curColor, (x, y), curLenght/2-1)
                startPos = x, y 

        elif cir_bool:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                startPos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
                endPos = pygame.mouse.get_pos()

                for col in colors:
                    if col.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curColor = col.color
                if eraser.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    screen.fill(WHITE)
                for size in length:
                    if size.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curLenght = size.color*2
                if cir.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = False
                    cir_bool = True
                if rect.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = True
                    cir_bool = False
                if pen.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = True
                    rect_bool = False
                x, y, a, b = min(startPos[0], endPos[0]), min(startPos[1], endPos[1]), max(startPos[0], endPos[0]), max(startPos[1], endPos[1])
                diam = min(a-x, b-y)
                pygame.draw.circle(screen, curColor, ((a-x)/2 + x, (b-y)/2 + y), diam/2)

        elif rect_bool:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                startPos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
                endPos = pygame.mouse.get_pos()
                for col in colors:
                    if col.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curColor = col.color
                if eraser.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    screen.fill(WHITE)
                for size in length:
                    if size.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                        curLenght = size.color*2
                if cir.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = False
                    cir_bool = True
                if rect.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = False
                    rect_bool = True
                    cir_bool = False
                if pen.hitbox.colliderect(pygame.Rect(endPos[0], endPos[1], 1, 1)) and endPos == startPos:
                    pen_bool = True
                    rect_bool = False
                    cir_bool = False
                x, y, a, b = min(startPos[0], endPos[0]), min(startPos[1], endPos[1]), max(startPos[0], endPos[0]), max(startPos[1], endPos[1])
                pygame.draw.rect(screen, curColor, (x, y, a-x, b-y))

    bg()
    clock.tick(30)
    pygame.display.flip()