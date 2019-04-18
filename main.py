

#		mypy\python work.py

import pygame
import math
import layout
from MyConst import *
import camera as cam


clock = pygame.time.Clock()
pygame.init()


#screen = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("This is caption app")


board=layout.Layout(screen);
board.draw_world()
   
   
NeighborActiveCell=[]

total_level_width=1200
total_level_height=1200
camera = cam.Camera(cam.camera_configure, total_level_width, total_level_height) 
cameraRect=[WIDTH_SCREEN/2,0]

isLeftPress=False
isRightPress=False

while PLAY:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			PLAY = False
		# elif event.type == pygame.VIDEORESIZE:
			# width, height = event.size
			# screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
		elif event.type == pygame.MOUSEMOTION:# Водим мышью по дисплею
			mouse_x=event.pos[0]
			mouse_y=event.pos[1]
		elif event.type ==  pygame.MOUSEBUTTONDOWN:
		
			
			for i in NeighborActiveCell:
				lastHex=i[0]
				lastHex.image=i[1]
				board.draw_world()
				
			mouse_x=event.pos[0]
			mouse_y=event.pos[1]
			print(cameraRect)
			mouse_x=mouse_x+cameraRect[0]-WIDTH_SCREEN/2
			# mouse_y=mouse_y+cameraRect[1]
			
			point=[mouse_x,mouse_y]
			print(point)

			
			collapsList=[]
			for hex in board.spriteGroup.sprites():
				if(hex.rect.collidepoint(point)):
					collapsList.append(hex)
			if(len(collapsList)!=0):
				spriteClck=collapsList[0]
				for hex in collapsList:
					if(spriteClck!=hex):
					#Формула вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости:
					#AB = √(xb - xa)2 + (yb - ya)2
						x1=spriteClck.rect.centerx
						y1=spriteClck.rect.centery
						x2=hex.rect.centerx
						y2=hex.rect.centery
						
						fromMouse_to_hex=math.sqrt(  (mouse_x-x2)*(mouse_x-x2) + (mouse_y-y2)*(mouse_y-y2) )
						fromMouse_to_spriteClck=math.sqrt(  (mouse_x-x1)*(mouse_x-x1) + (mouse_y-y1)*(mouse_y-y1) )
						# print("fromMouse_to_hex:"+str(fromMouse_to_hex))
						# print("fromMouse_to_spriteClck:"+str(fromMouse_to_spriteClck))
						if(fromMouse_to_spriteClck<=fromMouse_to_hex):
							spriteClck=spriteClck
						elif fromMouse_to_spriteClck>fromMouse_to_hex:
							spriteClck=hex
				
					
				listNeighbor=board.getListIndexNeighborHexFromIndexHex(spriteClck.index_x,spriteClck.index_y)
				# a=4/0
				# 222
				
				# x=spriteClck.index_x
				# y=spriteClck.index_y
				# self=board
				# 333
				NeighborActiveCell=[]
				Simage = pygame.image.load(r'image\border.png')
				image=pygame.transform.scale(Simage, TILE_SIZE)
				for i in listNeighbor:
					saveState=[]
					hex=board.hexList[i[0]][i[1]]
					saveState.append(hex);
					saveState.append(hex.image);
					NeighborActiveCell.append(saveState)
				
					hex.image=image;
				# print(str(spriteClck.index_x)+"|"+str(spriteClck.index_y))
				
				# print(str(hex.index_x)+"|"+str(hex.index_y))
				#hex.image.fill(GREEN)
				
				#board.draw_world()
				
					
		elif event.type == pygame.KEYDOWN:
			if( event.key == pygame.K_RIGHT):
				isRightPress=True
			elif event.key == pygame.K_LEFT:
				isLeftPress=True
				
		elif event.type == pygame.KEYUP:
			if( event.key == pygame.K_RIGHT):
				isRightPress=False
			elif event.key == pygame.K_LEFT:
				isLeftPress=False

				
		screen.fill(WHITE)	
		board.draw_camera(camera)

	if isLeftPress:
		move=cameraRect[0]-3
		cameraRect[0]=max(0,move)
		screen.fill(WHITE)	
		board.draw_camera(camera)
		
		
	if isRightPress: 
		move=max(WIDTH_SCREEN/2,cameraRect[0]+3);
		cameraRect[0]=min(move,1400)
		screen.fill(WHITE)	
		board.draw_camera(camera)

		
	camera.update(cameraRect[0],cameraRect[1])	
	

				
	pygame.display.flip()
 

	clock.tick(FPS)
