import pygame
import math

pygame.init()
screen = pygame.display.set_mode((480, 360))
done = False
clock = pygame.time.Clock()

x = 0
y = 180
OK = True
OKK = True

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

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    
    fs(x)
    fc(x)
    if OK: pygame.draw.line(screen, (255, 0, 0), (x, y + 175*fs(x)), (x + 3, y + 175*fs(x + 3)), 3)    
    pygame.draw.line(screen, (0, 0, 255), (x, y + 175*fc(x)), (x + 3, y + 175*fc(3 + x)), 3)


    pygame.display.flip()

    x += 3

    clock.tick(20)
pygame.quit()