import random

import pygame

from file import*



class Player:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []
    def draw(self, window):
        window.blit(self.texture, self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed

        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed

        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed

        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_v]:
            self.bullets.append(Bullet("bullet (1).png",
                                       20, 40,
                                       self.hitbox.x, self.hitbox.y,
                                       10))
        for bullet in self.bullets:
            bullet.move()



class Bullet:
    def __init__(self,  skin, width, height, x, y, speed):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        self.hitbox.y -= self.speed












class Enemy:
    def __init__(self, skin, width, height, x, y,speed):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        self.hitbox.y += self.speed








    def draw(self, window):
        window.blit(self.texture, self.hitbox)

























def game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    fps = pygame.time.Clock()
    data = read_from_file()
    player = Player(3, 65, 85, 147, 129, data['skin'])
    enemies = []
    y = 200
    for i in range(10):
        enemies.append(Enemy("ufo (1).png", 50, 50, random.randint(0, 650), y, 5))
        y -= 100


    score = data["score"]
    write_in_file(data)
    score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [0,0,0])




    background = pygame.image.load("galaxy (1).jpg")
    background = pygame.transform.scale(background, [700, 500])
    game = True


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        for e in enemies:
            for b in player.bullets:
                if e.hitbox.colliderect(b.hitbox):
                    b.hitbox.x = 5000
                    player.bullets.remove(b)
                    e.hitbox.y = -100
                    e.hitbox.x = random.randint(0, 650)
                    score += 1
                    data = read_from_file()
                    data["score"] = score
                    write_in_file(data)
                    break

        score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [255, 0, 255])




        player.move()
        window.fill([123, 123,  123])
        window.blit(background,[0, 0])
        player.draw(window)
        for e in enemies:
            e.draw(window)
        window.blit(score_lbl,[600, 10])
        pygame.display.flip()

        for e in enemies:
            e.move()
            if e.hitbox.y > 500:
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 650)















































        fps.tick(60)
