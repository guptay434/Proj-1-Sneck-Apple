import pygame
from pygame.locals import *


def drew_block():
    surface.fill((3, 4, 8))
    surface.blit(block, (block_x, block_y))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((3, 4, 8))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    pygame.display.update()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    running = False
                    
                if event.key == K_UP:
                    block_y -= 10
                    drew_block()

                if event.key == K_DOWN:
                    block_y += 10
                    drew_block()

                if event.key == K_LEFT:
                    block_x -= 10
                    drew_block()

                if event.key == K_RIGHT:
                    block_x += 10
                    drew_block()

            elif event.type == QUIT:
                running = False
