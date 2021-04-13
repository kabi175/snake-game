import pygame
import time 
from pygame.locals import *
from snake import Snake
from apple import Apple


class Game:
    def __init__(self,w=1000,h=500):
        pygame.init()
        self.s_width = w
        self.s_height = h
        self.crashed = False
        self.speed = 10
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.s_width,self.s_height])
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)
        self.score = 0
    
    def run(self):
        pygame.display.set_caption('Snake')
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        while not self.crashed:
            self.handle_event(self.snake)
            self.screen.fill((255, 255, 255))
            self.snake.move()            
            if self.apple.show(self.snake.snake[0]):
                self.score += 1
                self.snake.grow()

            pygame.display.flip()

            if self.snake.is_dashed():
                self.game_over()
            self.clock.tick(self.speed)

        pygame.quit()
    
    def handle_event(self,snake):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.crashed = True
                elif event.key == K_RIGHT:
                    snake.turn_right()
                elif event.key == K_LEFT:
                    snake.turn_left()
            elif event.type == QUIT:
                self.crashed = True
    
    def welcome(self):
        pass

    def game_over(self):
        self.screen.fill((0,0,0))
        pygame.display.flip()
        time.sleep(1)
        print("score",self.score)
        print("game over")
        self.crashed = True