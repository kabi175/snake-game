import pygame
import time 
from pygame.locals import *
from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.s_height = 500
        self.s_width = 1000
        self.screen = pygame.display.set_mode([self.s_width,self.s_height])
    
    def run(self):
        self.x,self.y = 0,0
        snake = Snake()
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        while True:
            time.sleep(0.2)
            self.screen.fill((255, 255, 255))
            snake.move(self.screen)
            pygame.display.flip()
            if self.update_event(snake) == True:
                pygame.quit()
                break
    
    def update_event(self,snake):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                elif event.key == K_RIGHT:
                    snake.turn_right()
                elif event.key == K_LEFT:
                    snake.turn_left()
                elif event.key == K_UP:
                    snake.grow()
            elif event.type == QUIT:
                return True
        return False
    
    def welcome(self):
        pass
    def game_over(self):
        pass