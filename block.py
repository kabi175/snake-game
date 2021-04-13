import pygame

class Block:
    def __init__(self,x=0,y=0,h=50,dir="RIGHT"):
        self.block = pygame.Surface((h, h))
        self.block.fill((0, 0, 0))
        self.pre_direction = dir
        self.direction = dir
        self.x,self.y = x,y

    def change_dir(self,dir):
        self.pre_direction = self.direction
        self.direction = dir
        
    def move(self,screen):
        if self.direction == "RIGHT":
            self.x += 50
        elif self.direction == "LEFT":
            self.x -= 50
        elif self.direction == "DOWN":
            self.y += 50
        elif self.direction == "UP":
            self.y -=50
        
        if self.x == 1000:
            self.x = 0
        elif self.y == 500:
            self.y = 0
        elif self.x < 0:
            self.x = 950
        elif self.y < 0:
            self.y = 450 
        screen.blit(self.block, (self.x, self.y))

    