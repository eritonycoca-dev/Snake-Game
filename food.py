import random
import pygame
from settings import WIDTH, HEIGHT, BLOCK_SIZE, RED


class Food:
    def __init__(self, snake_body, obstacles_positions):
        self.position = self.generate_position(snake_body, obstacles_positions)

    def generate_position(self, snake_body, obstacles_positions):
        while True:
            x = random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            pos = (x, y)
            
            if pos not in snake_body and pos not in obstacles_positions:
                return pos

    def draw(self, surface):
        pygame.draw.rect(surface, RED,
                         (self.position[0], self.position[1],
                          BLOCK_SIZE, BLOCK_SIZE))
        


