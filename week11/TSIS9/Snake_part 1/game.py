import pygame
import json
import random

#===========================================================
# дано

width = 750
height = 600

lvl = 0
score = 20
pygame.init()
pygame.display.set_caption("Snake by ALEX")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 25)
done = False
walls = []
players = []
food = []
images = {}
pygame.mixer.music.load(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\music\menu.mp3')
pygame.mixer.music.play(loops= -1)
#===========================================================
# классы


class Food:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.x_size = 19
        self.y_size = 21
        self.hitbox = pygame.Rect(self.x, self.y, self.x_size, self.y_size)
        self.number = number
    def draw(self):
        screen.blit(images[self.number], (self.x, self.y))
    def load_hitbox(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.x_size, self.y_size)
    def collision(self):
        global score
        for block in walls:
            if self.hitbox.colliderect(block.hitbox):
                self.x = random.randint(0, 750)
                self.y = random.randint(0, 600)
                self.number = random.randint(1, 4)
                self.hitbox = pygame.Rect(self.x, self.y, self.x_size, self.y_size)
        for player in players:
            for hitboxes in player.hitbox:
                if self.hitbox.colliderect(hitboxes):
                    self.x = random.randint(0, 750)
                    self.y = random.randint(0, 600)
                    self.number = random.randint(1, 4)
                    score += 1
                    player.add_length()
    def respawn(self):
        self.x = random.randint(0, 750)
        self.y = random.randint(0, 600)
        self.number = random.randint(1, 4)
        

class Wall:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 3)
        pygame.draw.rect(screen, self.color, (self.x+5, self.y+5, self.width-10, self.height-10))

class Snakes:
    def __init__ (self, x, y, speed, size, color, control):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.length = 3
        self.color = color
        self.control = control
        if self.control == "RED": self.direction = "DOWN"
        else: self.direction = "UP"
        self.hitbox = [pygame.Rect(self.x, self.y, self.size, self.size)]
        self.xy = [[self.x, self.y]]
        self.hitbox_head = pygame.Rect(self.x, self.y, self.size, self.size)
    def pressed(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.control == "BLUE" and self.direction != "DOWN": self.direction = "UP"
        if pressed[pygame.K_DOWN] and self.control == "BLUE" and self.direction != "UP": self.direction = "DOWN"
        if pressed[pygame.K_LEFT] and self.control == "BLUE" and self.direction != "RIGHT": self.direction = "LEFT"
        if pressed[pygame.K_RIGHT] and self.control == "BLUE" and self.direction != "LEFT": self.direction = "RIGHT"
        if pressed[pygame.K_w] and self.control == "RED" and self.direction != "DOWN": self.direction = "UP"
        if pressed[pygame.K_s] and self.control == "RED" and self.direction != "UP": self.direction = "DOWN"
        if pressed[pygame.K_a] and self.control == "RED" and self.direction != "RIGHT": self.direction = "LEFT"
        if pressed[pygame.K_d] and self.control == "RED" and self.direction != "LEFT": self.direction = "RIGHT"
    def move(self):
        self.xy.append([self.x, self.y])
        self.hitbox.append(pygame.Rect(self.x, self.y, self.size, self.size))
        if self.direction == "UP": self.y -= self.speed
        if self.direction == "DOWN": self.y += self.speed
        if self.direction == "RIGHT": self.x += self.speed
        if self.direction == "LEFT": self.x -= self.speed
        self.hitbox_head = pygame.Rect(self.x, self.y, self.size, self.size)
        while len(self.xy) > self.length: 
            self.xy.pop(0)
            self.hitbox.pop(0)
    def add_length(self):
        self.length += 1
    def draw(self):
        for element in self.xy:
            pygame.draw.rect(screen, self.color, (element[0], element[1], self.size, self.size))
    def collision(self):
        global done
        for player in players:
            for boxes in player.hitbox:
                if self.hitbox_head.colliderect(boxes): done = True
        for block in walls:
            if self.hitbox_head.colliderect(block.hitbox): done = True


#===========================================================
# функции

def get_image(path):
    global my_images
    image = pygame.image.load(path)
    if image == None:
        cannonicalazid_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(cannonicalized_path)
        my_images[path] = image
    return image


def map(lvl):
    global walls
    walls.clear()
    with open(f'C:/Users/Мои документы/Desktop/Универ/1 курс 2 семестр/PP2/alex/week11/TSIS9/Snake_part 1/maps/map{lvl}', 'r') as f:
        row_ind = 0
        for rows in f:
            for blocks_ind in range(len(rows)):
                if rows[blocks_ind] == '1': 
                    walls.append(Wall(blocks_ind*30, row_ind*30, ((13*row_ind) % 256, (11*blocks_ind) % 256, 190), 30, 30))
            row_ind += 1

def play():
    screen.fill((51, 53, 67))
    screen.blit(font.render("Score: " + str(score) + "/20", 1, (50, 0, 200)), (width - 190, 25))
    for block in walls:
        block.draw()
    for player in players:
        player.pressed()
        player.move()
        player.draw()
        player.collision()
    for fruits in food:
        fruits.draw()
        fruits.collision()
        fruits.load_hitbox()

def menu(): 
    screen.blit(menu_image, (-50, -170))
    screen.blit(pygame.font.SysFont('comicsansms', 25).render("Press SPACE to begin", 1, (0, 100, 200)), (10, 10))
    screen.blit(pygame.font.SysFont('comicsansms', 25).render("Press ESC to exit", 1, (0, 100, 200)), (10, 40))


def paused():
    screen.blit(pygame.font.SysFont('comicsansms', 100).render("PAUSE", 1, (0, 255, 0)), (width/2 - 150, 140))
    screen.blit(pygame.font.SysFont('comicsansms', 40).render("press s to save", 1, (0, 255, 0)), (width/2 - 150, 250))
    screen.blit(pygame.font.SysFont('comicsansms', 40).render("press l to load", 1, (0, 255, 0)), (width/2 - 150, 300))

def save(players, food, lvl):
    stats = {
            "player1":[players[0].x, players[0].y, players[0].length, players[0].direction, players[0].xy], 
            "player2":[players[1].x, players[1].y, players[1].length, players[1].direction, players[1].xy],
            "lvl": lvl,
            "food1": [food[0].x, food[0].y, food[0].number],
            "food2": [food[1].x, food[1].y, food[1].number],
            "food3": [food[2].x, food[2].y, food[2].number],
            "food4": [food[3].x, food[3].y, food[3].number],
            "score": score
            }
    with open(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\saved_game.json', 'w') as file:
        json.dump(stats, file)


def load():
    global lvl, score
    stats = {}
    try:
        with open(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\saved_game.json', 'r') as file:
            stats = json.load(file)
    except: print("empty")
    players[0].x = stats["player1"][0]
    players[0].y = stats["player1"][1]
    players[0].length = stats["player1"][2]
    players[0].direction = stats["player1"][3]
    players[0].xy = stats["player1"][4]
    players[1].x = stats["player2"][0]
    players[1].y = stats["player2"][1]
    players[1].length = stats["player2"][2]
    players[1].direction = stats["player2"][3]
    players[1].xy = stats["player2"][4]
    lvl = stats["lvl"]
    food[0].x = stats["food1"][0]
    food[0].y = stats["food1"][1]
    food[0].number = stats["food1"][2]
    food[1].x = stats["food2"][0]
    food[1].y = stats["food2"][1]
    food[1].number = stats["food2"][2]
    food[2].x = stats["food3"][0]
    food[2].y = stats["food3"][1]
    food[2].number = stats["food3"][2]
    food[3].x = stats["food4"][0]
    food[3].y = stats["food4"][1]
    food[3].number = stats["food4"][2]
    for fruits in food:
        fruits.load_hitbox()
    score = stats["score"]
    map(lvl)
    play()



#===========================================================
# добавление

players.append(Snakes(width-100, height-100, 10, 10, (0, 0, 255), "BLUE"))
players.append(Snakes(100, 100, 10, 10, (255, 0, 0), "RED"))
for i in range(4):
    food.append(Food(random.randint(0, 750), random.randint(0, 600), random.randint(1, 4)))
images[1] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\foods\GreenApple.png')
images[2] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\foods\RedApple.png')
images[3] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\foods\Cherry.png')
images[4] = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\foods\Banana.png')
menu_image = get_image(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\snake_image.png')

#===========================================================
# игра


while not done:
    button = pygame.key.get_pressed()
    for event in pygame.event.get():
        if button[pygame.K_SPACE] or event.type == pygame.QUIT: done = True
        if button[pygame.K_ESCAPE]: exit()

    menu()

    clock.tick(30)
    pygame.display.flip()

pygame.mixer.music.load(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\music\game.mp3')
pygame.mixer.music.play(loops= -1)

done = False
pause = False

while not done:
    button = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        if button[pygame.K_SPACE]: 
            pause = not pause

    while pause: 
        button = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True
            if button[pygame.K_SPACE]: pause = not pause
            if button[pygame.K_s]: save(players, food, lvl)
            if button[pygame.K_l]: load()

        paused()

        clock.tick(30)
        pygame.display.flip()

    if score >= 20:
        if lvl <= 6: lvl += 1
        else: lvl = 1
        map(lvl)
        score = 0
        for fruits in food:
            fruits.respawn()
        for player in players:
            player.length = 3
            if player.control == "RED":
                player.x = 100
                player.y = 100
                player.direction = "DOWN"
            elif player.control == "BLUE":
                player.x = width - 100
                player.y = height - 100
                player.direction = "UP"


    play()
    clock.tick(16)
    pygame.display.flip()


pygame.mixer.music.load(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week11\TSIS9\Snake_part 1\music\gameover.mp3')
pygame.mixer.music.play()

while done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT: done = False

    screen.blit(pygame.font.SysFont('comicsansms', 100).render("GAME OVER", 1, (0, 255, 0)), (width/2 - 300, 160))

    clock.tick(16)
    pygame.display.flip()