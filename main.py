import pygame




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
                                       10,10,
                                       self.hitbox.x + 28, self.hitbox.y,
                                       10))




        for bullet in self.bullets:
            bullet.move()




class Bullet:
    def __init__(self, skin, width, height, x, y, speed):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed





    def move(self):
        self.hitbox.y -= self.speed



    def draw(self, window):
        window.blit(self.texture, self.hitbox)

















class Enemy:
    def __init__(self, speed, width, height, x, y, skin):
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


























pygame.init()
window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()
player = Player(3, 65, 85, 250, 400, "rocket (1).png")
enemy = Enemy(5, 55, 45, 147, 129, "ufo (1).png")
background = pygame.image.load("galaxy (1).jpg")
background = pygame.transform.scale(background, [700, 500])
game = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    enemy.move()
    player.move()
    window.fill([123, 123,  123])
    window.blit(background,[0, 0])
    player.draw(window)
    enemy.draw(window)
    pygame.display.flip()




























































    fps.tick(60)
