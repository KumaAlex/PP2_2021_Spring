import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 600))
done = False
clock = pygame.time.Clock()
fall = []

step = 20
x = 20
score = 0
of = 0

class circles():
    def __init__ (self, x, y, color, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color
    def move(self):
        self.y += self.speed
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def winUpdate():
    spawner()
    for go in fall:
        global of
        go.draw()
        go.move()
        if go.y > 640:
            fall.remove(go)
            of += 1
        elif (go.y in range(550 - go.radius, 571 - go.radius) or go.y in range(550, 571)) and (go.x in range(x, x+101) or go.x in range(x - go.radius, x + 101 + go.radius) or go.x in range(x + go.radius, x + 101 - go.radius)):
            fall.remove(go)
            global score
            of += 1
            score += 1


def spawner():
    if len(fall) < 7:
        fall.append(circles(random.randint(40, 960), -40, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(3, 10), random.randint(10, 40)))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    
    screen.fill((150, 150, 150))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x >= 20: x -= step
    if pressed[pygame.K_RIGHT] and x <= 880: x += step

    pygame.draw.rect(screen, (200, 255, 0), (x, 550, 100, 20))

    winUpdate()

    pygame.display.flip()

    clock.tick(30)

print("Your score: " + str(score) + " of " + str(of))

pygame.quit()