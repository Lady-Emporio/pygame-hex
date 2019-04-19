import pygame
from MyConst import *
def camera_configure(camera, x,y):
    l=x
    t=y
    _, _, w, h = camera
    # l, t = -l+WIDTH_SCREEN / 2, -t+HEIGHT_SCREEN / 2
    l, t = -l, -t

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIDTH_SCREEN), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-HEIGHT_SCREEN), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)   

class Camera(object):
    def __init__(self, camera_func, width, height,x,y):
        self.camera_func = camera_func
        self.state = pygame.Rect(x, y, width, height)
        self.x=x
        self.y=y
        self.moveInOneFPS=7
	
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self):
        self.state = self.camera_func(self.state, self.x,self.y)