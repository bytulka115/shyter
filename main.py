import pygame




class Player:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed





    def move(self):
        keys = pygame.key.get_pressed()
        self.xodba.set_volume(0)
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
            self.xodba.set_volume(1)
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
            self.xodba.set_volume(1)
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
            self.xodba.set_volume(1)
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
            self.xodba.set_volume(1)






    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def draw(self, window):
        window.blit(self.texture, self.hitbox)
























pygame.init()
window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()
player = Player(3, 55, 45, 147, 129, "rocket (1).png")
background = pygame.image.load("galaxy (1).jpg")
background = pygame.transform.scale(background, [700, 500])
game = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    window.fill([123, 123,  123])
    window.blit(background,[0, 0])
    pygame.display.flip()




























































    fps.tick(60)
