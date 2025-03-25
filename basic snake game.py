#basic snake game 

import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení obrazovky
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Barvy
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializace hada a jídla
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (BLOCK_SIZE, 0)
food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Ovládání
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
    
    # Pohyb hada
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False  # Game Over
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                    random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
        else:
            snake.pop()
    
    # Vykreslení hada
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Vykreslení jídla
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
