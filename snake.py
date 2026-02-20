import pygame  
from settings import BLOCK_SIZE, Initial_speed , Speed_Increment, Level_Up_Food 

class Snake: 
    def __init__(self, name): 
        self .name = name 
        self .body = [(100, 100), (80, 100), (60, 100)]
        self .direction = "RIGHT"
        self .grow = False 
        self.food_eaten= 0
        self.speed = Initial_speed 
    
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

    def grow_snake(self):
        self.grow=True 
        self.food_eaten += 1

        if self.food_eaten % Level_Up_Food  == 0:
            self.speed += Speed_Increment  

    def change_direction(self, new_direction): 
        opposite = {
            "UP": "DOWN", 
            "DOWN": "UP", 
            "LEFT": "RIGHT", 
            "RIGHT": "LEFT" 
        }
        if new_direction != opposite[self.direction]: 
            self.direction = new_direction

    def check_self_collision(self):
        return self.body[0] in self.body[1:]
    
    def draw(self, surface):
        # Degradado dinámico
        for index, segment in enumerate(self.body):
            green_intesity = max(50,255 - index * 10)
            color=(0, green_intesity, 0)
            pygame.draw.rect(surface, color,
                             (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE)) 
    
    
    def grow_snake(self):
        self.grow = True 
         
