
from MyConst import *
import pygame
pygame.init()


class NPS(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		Simage = pygame.image.load(r'image\nps1.png')
		self.defaultImage=pygame.transform.scale(Simage, [int(TILE_SIZE[0]/2),int(TILE_SIZE[1]/2)])
		Simage = pygame.image.load(r'image\border.png')
		self.activeImage=pygame.transform.scale(Simage, [int(TILE_SIZE[0]/2),int(TILE_SIZE[1]/2)])
		self.image=self.defaultImage
		self.rect = self.image.get_rect()
		self.active=False
		
		self.updateIndex=0;
	def draw(self,display):
		if self.active:
			display.blit(self.defaultImage,(0,0))
			display.blit(self.activeImage,(0,0))
		else:
			display.blit(self.defaultImage,(0,0))
	def __nonzero__(self):
		return True
	def update(self):
		self.updateIndex+=1
		# self.defaultImage.rect.move(10, 0)
		# self.activeImage.rect.move(10, 0)
		
class Detail():
	def __init__(self, display):
		self.display = display;
		self.firstNps=NPS()
		self.draw_all()
	def draw_all(self):
		self.display.fill(GREEN)
		self.firstNps.draw(self.display)