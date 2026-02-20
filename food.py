# food.py 

import random 
from settings import WIDTH, HEIGHT, BLOCK_SIZE, RED 
import pygame 

class Food: 

    def __init__(self, snake_body, obstacles):
        self.position = self.generate_position(snake_body, obstacles)

    def generate_position(self, snake_body, obstacles):
          while True: 
            x = random.randarage(0, WIDTH, BLOCK_SIZE)
            y = random.randrange(0, HEIGHT, BLOCK_SIZE)

            if (x, y) not in snake_body and (x, y) not in obstacles: 
                return (x, y)
    
    def draw(self, surface): 
        pygame.draw.rect(surface, RED,
                         (self.position[0], self.position[1], 
                          BLOCK_SIZE, BLOCK_SIZE))
        

