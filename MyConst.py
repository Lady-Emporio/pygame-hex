

import pygame
pygame.init()#Its must be second init - repeated calls will have no effect.
FONT = pygame.font.SysFont('arial', 10)

FPS=30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653
WIDTH_SCREEN=600
HEIGHT_SCREEN=400
HEIGHT_SETTINGS=200
SIZE = (WIDTH_SCREEN, HEIGHT_SCREEN+HEIGHT_SETTINGS)
PLAY = True

# Если TILE_SIZE = (60, 70)  то лучше ставить 20 расстояние
# DEL_SPACE_BEETWEEN_HEX должен быть равен 20.
# TILE_SIZE = (120, 120) лучше ставить 30 расстояние
# DEL_SPACE_BEETWEEN_HEX=30	
#
# TILE_SIZE = (60, 70) #Что это? image = pygame.transform.scale(image, TILE_SIZE)
TILE_SIZE = (120, 120) 
DEL_SPACE_BEETWEEN_HEX=30			



