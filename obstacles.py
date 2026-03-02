import random
import pygame
from settings import WIDTH, HEIGHT, BLOCK_SIZE, OBSTACLE_COUNT, BROWN


class Obstacles:  
    def __init__(self, snake_body):
        self.positions = self.generate_obstacles(snake_body)

    def generate_obstacles(self, snake_body):
        positions = []  

        attempts = 0
        max_attempts = 500  

        while len(positions) < OBSTACLE_COUNT and attempts < max_attempts:
            x = random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            pos = (x, y)

            if pos not in snake_body and pos not in positions:
                positions.append(pos)

            attempts += 1

        return positions

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, BROWN,
                             (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
