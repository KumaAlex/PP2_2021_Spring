import pygame
import math

pygame.init()
screen = pygame.display.set_mode((634, 500))
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)
x = 0
y = 250
OK = True
OKK = True

def bg():
    screen.fill((230, 230, 230))

    for i in range(9):
        screen.blit(font.render(str(float(1 - 0.25*i)), 1, (0, 0, 0)), (7, 40 + i*50))

    for i in range(9):
        a = 1
        if i == 0 or i == 4 or i == 8: a = 2
        pygame.draw.line(screen, (0, 0, 0), (49, 50 + i*50), (583, 50 + i*50), a)
    
    for i in range(7):
        a = 1
        if i == 0 or i == 3 or i == 6: a = 2
        pygame.draw.line(screen, (0, 0, 0), (49 + i*88.78, 50), (49 + i*88.78, 450), a)

    j = -3.5
    for i in range(13):
        j += 0.5
        if int(j) != j and j != 0: screen.blit(font.render(str(float(j))+'п', 1, (0, 0, 0)), (30 + i*45, 460))
        elif j == 0: screen.blit(font.render('0', 1, (0, 0, 0)), (42 + i*45, 460))
        else: screen.blit(font.render(str(int(j))+'п', 1, (0, 0, 0)), (36 + i*45, 460))

    for i in range(6):
        pygame.draw.line(screen, (0, 0, 0), (94 + i*88.78, 443), (94 + i*88.78, 450))
        pygame.draw.line(screen, (0, 0, 0), (94 + i*88.78, 50), (94 + i*88.78, 57))


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
        if OK: pygame.draw.line(screen, (0, 0, 255), (x + n + 50, y + 200*fc(x)), (x + n + 3 + 50, y + 200*fc(x + 3)), 3)    
        pygame.draw.line(screen, (255, 0, 0), (x + 50 + n, y + 200*fs(x)), (x + n + 50 + 3, y + 200*fs(3 + x)), 3)


    pygame.display.flip()

    x += 3
    n += 1

    clock.tick(30)
pygame.quit()