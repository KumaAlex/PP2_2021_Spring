import pygame
import random

pygame.init()
pygame.display.set_caption("MyGame_ALEX")
screen = pygame.display.set_mode((800, 600))
pygame.mixer.music.load(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\kevin-macleod-pixelland.mp3')
pygame.mixer.music.play(loops= -1)
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 20)
done = False
my_images = {}
score = 0
bonuses = 0
speed = 5

def get_image(path):
    global my_images
    image = pygame.image.load(path)
    if image == None:
        cannonicalazid_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(cannonicalized_path)
        my_images[path] = image
    return image

def getting_Im():
    coin1 = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\coin(1).png')
    coin2 = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\coin(2).png')
    coin3 = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\coin(3).png')
    coin4 = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\coin(4).png')
    global coinAnim, my_images
    coinAnim = (coin1, coin2, coin3, coin4)
    my_images['Car'] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\Player.png')
    my_images['Enemy'] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\Enemy.png')
    my_images['Bonus'] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\Bonus.png')

getting_Im()

def bg():
    screen.fill((100, 200, 100))
    pygame.draw.rect(screen, (100, 100, 100), (150, 0, 500, 650))
    screen.blit(my_images['Bonus'], (655, 140))
    screen.blit(font.render("speed - 3", 1, (50, 0, 200)), (705, 150))

class rect:
    def __init__(self, x, y, x_, y_):
        self.x = x
        self.y = y
        self.speed = speed
        self.x_ = x_
        self.y_ = y_
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.x_, self.y_))
    def move(self):
        self.speed = speed
        self.y += self.speed
    def back(self):
        if self.y >= 600: self.y -= 750

class Enemy():
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.enemy_hitbox = pygame.Rect(self.x, self.y, 44, 96)
    def move(self):
        self.y += self.speed
        self.enemy_hitbox = pygame.Rect(self.x, self.y, 44, 96)
    def draw(self):
        screen.blit(my_images['Enemy'], (self.x, self.y))
    def back(self):
        if self.y >= 700:
            self.speed = random.randint(int(speed + 0.5), int(speed + 0.5) + 5)
            self.x = random.randint(250, 650 - 44)
            self.y = random.randint(-400, -100)
        if self.enemy_hitbox.colliderect(car.car_hitbox):
            global done
            done = True

class player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.car_hitbox = pygame.Rect(self.x, self.y, 44, 96)
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.x > 150: self.x -= 10
        if pressed[pygame.K_RIGHT] and self.x < 606: self.x += 10
        self.car_hitbox = pygame.Rect(self.x, self.y, 44, 96)
    def draw(self):
        screen.blit(my_images['Car'], (self.x, self.y))

q = -1

class coin:
    def __init__(self, x, y, OK):
        self.OK = OK
        self.x = x
        self.y = y
        self.speed = speed
        self.coin_hitbox = pygame.Rect(self.x-50, self.y-50, 100, 100)
    def draw(self):
        global q
        q += 1
        if q == 64: q = 0
        if self.OK == False: screen.blit(coinAnim[int(q/16)], (self.x, self.y))
        else: screen.blit(my_images['Bonus'], (self.x, self.y))
    def move(self):
        self.coin_hitbox = pygame.Rect(self.x-50, self.y-50, 100, 100)
        self.speed = speed
        self.y += self.speed
    def back(self):
        if self.y >= 600:
            self.x = random.randint(250, 550)
            if self.OK == False: self.y = random.randint(-700, -100)
            else: self.y = random.randint(-5000, -3000)
        if self.coin_hitbox.colliderect(car.car_hitbox):
            self.x = random.randint(250, 550)
            if self.OK == False:
                self.y = random.randint(-700, -100)
                global score
                score += 1
            else:
                self.y = random.randint(-5000, -3000)
                global speed, bonuses
                bonuses += 1
                speed -= 3


car = player(378, 450)
enemy = Enemy(random.randint(250, 650 - 44), random.randint(-400, -100), random.randint(speed, speed + 3))
coins = []
rects = []
for i in range(5):
    rects.append(rect(250, i*150 - 150, 50, 100))
    rects.append(rect(500, 150*i - 150, 50, 100))
for i in range(3):
    coins.append(coin(random.randint(250, 550), random.randint(-500, -100), False))
coins.append(coin(random.randint(255, 550), random.randint(-5000, -3000), True))

def play():
    bg()
    for i in rects:
        i.draw()
        i.move()
        i.back()
    for i in coins:
        i.draw()
        i.move()
        i.back()
    enemy.draw()
    enemy.move()
    enemy.back()
    car.draw()
    car.move()
    screen.blit(font.render("Coins: " + str(score), 1, (50, 0, 200)), (670, 30))
    screen.blit(font.render("Bonuses: " + str(bonuses), 1, (50, 0, 200)), (670, 60))
    screen.blit(font.render("Speed: " + str(speed), 1, (50, 0, 200)), (670, 90))

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)

while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED: speed += 0.5  
        if event.type == pygame.QUIT: done = True

    play()

    clock.tick(60)
    pygame.display.flip()

done = False

screen.fill((255, 0, 0))

pygame.mixer.music.load(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\games\TSIS8\pohoronnij-marsh-8-bit.mp3')
pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    
    screen.blit(pygame.font.SysFont('comicsansms', 100).render("GAME OVER", 1, (50, 100, 200)), (100, 150))
    screen.blit(pygame.font.SysFont('comicsansms', 100).render("SCORE: " + str(score), 1, (50, 100, 200)), (170, 250))

    clock.tick(30)
    pygame.display.flip()