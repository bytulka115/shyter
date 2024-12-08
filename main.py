import pygame

pygame.init()
window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()


def draw(self, window):
    window.blit(self.texture, self.hitbox)


fps.tick(60)
