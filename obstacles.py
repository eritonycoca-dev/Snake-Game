import random 
import pygame
from settings import WIDTH, HEIGHT, BLOCK_SIZE, OBSTACLE_COUNT, GRAY 

class obstacles: 

    def __init__(self, snake_body):
        self.positions= self.generate_obstacles(snake_body)

    def generate_obstacles(self, snake_body):
        Obstacles = []

        while len(obstacles) < OBSTACLE_COUNT:
            x= random.randrange(0, WIDTH, BLOCK_SIZE)
            y= random.randrange(0, HEIGHT, BLOCK_SIZE)

            if (x, y) not in snake_body and (x, y) not in Obstacles:
                Obstacles.append((x, y))

        return obstacles 
    
def draw(self, surface):
    for pos in self.positions:
        pygame.draw.rect(surface, GRAY,
                         (pos[0], pos[1],   BLOCK_SIZE, BLOCK_SIZE))
