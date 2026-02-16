import pygame 
from settings import BLOCK_SIZE, GREEN 

class Snake: 
    def __init__(self, name): 
        self .name = name 
        self .body = [(100, 100), (80, 100), (60, 100)]
        self .direction = "RIGHT"
        self .grow = False 
    
    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - BLOCK_SIZE)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + BLOCK_SIZE)
        elif self.direction == "LEFT":
            new_head = (head_x - BLOCK_SIZE, head_y)
        elif self.direction == "RIGHT": 
            new_head = (head_x + BLOCK_SIZE, head_y)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else: 
            self.grow = False 

    def change_direction(self, new_direction): 
        opposite = {
            "UP": "DOWN", 
            "DOWN": "UP", 
            "LEFT": "RIGHT", 
            "RIGHT": "LEFT" 
        }
        if new_direction != opposite[self.direction]: 
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body: 
            pygame.draw.rect(surface, GREEN,
                             (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            
    def check_self_collision(self):
        return self.body[0] in self.body[1:]
    
    def grow_snake(self):
        self.grow = True 
         
