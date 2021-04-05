import pygame
import math

pygame.init()
screen = pygame.display.set_mode((684, 550))
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)
x = 0
y = 250
OK = True
OKK = True

def bg():
    screen.fill((230, 230, 230))

    # левые значения
    for i in range(9):
        screen.blit(font.render(str(float(1 - 0.25*i)), 1, (0, 0, 0)), (7, 40 + i*50))

    # горизонтальные линии
    for i in range(9):
        a = 1
        if i == 0 or i == 4 or i == 8: a = 2
        pygame.draw.line(screen, (0, 0, 0), (59, 50 + i*50), (623, 50 + i*50), a)
    
    # вертикальные линии
    for i in range(7):
        a = 1
        if i == 0 or i == 3 or i == 6: a = 2
        pygame.draw.line(screen, (0, 0, 0), (74 + i*88.78, 35), (74 + i*88.78, 465), a)

    # нижние значения
    j = -3.5
    for i in range(13):
        j += 0.5
        if int(j) != j and j != 0: screen.blit(font.render(str(float(j))+'п', 1, (0, 0, 0)), (55 + i*45, 475))
        elif j == 0: screen.blit(font.render('0', 1, (0, 0, 0)), (67 + i*45, 475))
        else: screen.blit(font.render(str(int(j))+'п', 1, (0, 0, 0)), (61 + i*45, 475))

    # вертикальные зубчики
    for i in range(6):
        pygame.draw.line(screen, (0, 0, 0), (119 + i*88.78, 458), (119 + i*88.78, 465))
        pygame.draw.line(screen, (0, 0, 0), (119 + i*88.78, 35), (119 + i*88.78, 42))

    # боковые зубчики
    for i in range(8):
        pygame.draw.line(screen, (0, 0, 0), (59, 75 + i*50), (66, 75 + i*50), 1)
        pygame.draw.line(screen, (0, 0, 0), (616, 75 + i*50), (623, 75 + i*50), 1)

    # внешняя рамка
    pygame.draw.line(screen, (0, 0, 0), (59, 35), (623, 35), 2) #в
    pygame.draw.line(screen, (0, 0, 0), (623, 35), (623, 465), 2) #п
    pygame.draw.line(screen, (0, 0, 0), (59, 35), (59, 465), 2) #л
    pygame.draw.line(screen, (0, 0, 0), (623, 465), (59, 465), 2) #н

    screen.blit(font.render("sin", 1, (255, 0, 0)), (30, 520))
    screen.blit(font.render("cos", 1, (0, 0, 255)), (30, 500))
    pygame.draw.line(screen, (255, 0, 0), (60, 534), (110, 534))
    for i in range(0, 5, 2):
        pygame.draw.line(screen, (0, 0, 255), (60 + 10*i, 514), (60 + 10 + 10*i, 514))

bg()

def fs(x):
    global OK
    OK = not OK
    y = math.sin(x)
    if OK:
        y *= -1
    return(y)

def fc(x):
    global OKK
    OKK = not OKK
    y = math.sin(x + 300)
    if OKK:
        y *= -1
    return(y)

n = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    
    if x <= 398:
        fs(x)
        fc(x)
        if OK: pygame.draw.line(screen, (0, 0, 255), (x + n + 75, y + 200*fc(x)), (x + n + 3 + 75, y + 200*fc(x + 3)), 3)    
        pygame.draw.line(screen, (255, 0, 0), (x + 75 + n, y + 200*fs(x)), (x + n + 75 + 3, y + 200*fs(3 + x)), 3)


    pygame.display.flip()

    x += 3
    n += 1

    clock.tick(30)
pygame.quit()