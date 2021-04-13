from block import Block
class Snake:
    def __init__(self,length=3):
        self.snake_len = length
        self.snake = []
        while length:
            length -= 1
            self.snake.append(Block(x=50*length,y=0))
    
    def move(self,screen):
        for index in range (1,len(self.snake)):
            self.snake[index].change_dir(self.snake[index-1].pre_direction)
        for block in self.snake:
            block.move(screen)
        self.snake[0].change_dir(self.snake[0].direction)

    def turn_right(self):
        if self.snake[0].direction == "RIGHT":
            self.snake[0].change_dir("DOWN")
        elif self.snake[0].direction == "DOWN":
            self.snake[0].change_dir("LEFT")
        elif self.snake[0].direction == "LEFT":
            self.snake[0].change_dir("UP")
        elif self.snake[0].direction == "UP":
            self.snake[0].change_dir("RIGHT")

    def turn_left(self):
        self.head_direction = self.snake[0].direction
        if self.snake[0].direction == "RIGHT":
            self.snake[0].change_dir("UP")
        elif self.snake[0].direction == "UP":
            self.snake[0].change_dir("LEFT")
        elif self.snake[0].direction == "LEFT":
            self.snake[0].change_dir("DOWN")
        elif self.snake[0].direction == "DOWN":
            self.snake[0].change_dir("RIGHT")
    
    def grow(self):
        x,y,pdir,dir= self.snake[self.snake_len-1].x , self.snake[self.snake_len-1].y,self.snake[self.snake_len-1].pre_direction,self.snake[self.snake_len-1].direction
        if dir == "RIGHT":
            x -= 50
        elif dir == "LEFT":
            x += 50
        elif dir == "UP":
            y += 50
        elif dir == "DOWN":
            y -= 50
        self.snake.append(Block(x=x,y=y,dir=pdir))
        self.snake_len+=1
    
    def is_dashed(self):
        return False