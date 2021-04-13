import random
import pygame

class Apple:
    def __init__(self,screen):
        self.screen = screen
        self.apple = pygame.Surface((50, 50))
        self.apple.fill((237, 12, 31))
        self.x = 0
        self.y = 0
        self.spawn()
    
    def spawn(self,w=950,h=450):
        self.x = random.randint(0,w/50)*50
        self.y = random.randint(0,h/50)*50
    
    def show(self,head)-> bool:
        captured = False
        if head.x == self.x and head.y == self.y:
            self.spawn()
            captured = True
        self.screen.blit(self.apple, (self.x, self.y))
        return captured

