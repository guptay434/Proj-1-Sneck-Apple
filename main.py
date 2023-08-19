# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:02:48 2023

@author: L1061343
"""

import pygame
from pygame.locals import *
import time

def drew_block():
    surface.fill((3,4,8))
    surafce.blit(block,(block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((500,500))
    surface.fill((3,4,8))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x =100
    block_y = 100
    surface.blit(block,(block_x, block_y))
    
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            
            if event.key == K_UP:
                block_y += 10
                drew_block()
                
            if event.key == K_DOWN:
                block_y -= 10
                drew_block()
            
            if event.key == K_LEFT:
                block_x -= 10
                drew_block()
                
            if event.key == K_RIGHT:
                block_x += 10
                drew_block()
                
            elif event.type == QUIT:
                running = False