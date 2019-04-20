

#		mypy\python work.py

import pygame
import math
import layout
from MyConst import *
import camera as cam
from detail import Detail

clock = pygame.time.Clock()
pygame.init()


#screen = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
display = pygame.display.set_mode(SIZE)

screen=display.subsurface((0,0,WIDTH_SCREEN, HEIGHT_SCREEN))

settings=display.subsurface((0,HEIGHT_SCREEN,WIDTH_SCREEN, SIZE[1]-HEIGHT_SCREEN))
detail=Detail(settings)

pygame.display.set_caption("This is caption app")



board=layout.Layout(screen);
#board.draw_world()
   
   
NeighborActiveCell=[]

total_level_width=1200
total_level_height=1200
camera = cam.Camera(cam.camera_configure, total_level_width, total_level_height,0,0) 

isLeftPress=False
isRightPress=False
isTopPress=False
isDownPress=False
needUpdateList=[]
while PLAY:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			PLAY = False
			
		elif event.type == pygame.VIDEORESIZE:
			print("TODO VIDEORESIZE")
		elif event.type == pygame.MOUSEMOTION:# Водим мышью по дисплею
			mouse_x=event.pos[0]
			mouse_y=event.pos[1]
		elif event.type ==  pygame.MOUSEBUTTONDOWN:
			if event.button == 1:#left mouse button
				mouse_x=event.pos[0]
				mouse_y=event.pos[1]
				if(mouse_x > screen.get_width() or mouse_y > screen.get_height()):
					#Клик по Detail
					if(detail.firstNps.rect.collidepoint(mouse_x, mouse_y-HEIGHT_SCREEN) ):
					
						detail.firstNps.active=True
						board.activeNps=detail.firstNps
						board.activeHex=False
					else:
						detail.firstNps.active=False
						board.activeNps=False
					
				
				else:
			
					for i in NeighborActiveCell:
						lastHex=i[0]
						lastHex.image=i[1]
						#board.draw_world()
				
					mouse_x=mouse_x+camera.x
					mouse_y=mouse_y+camera.y
					point=[mouse_x,mouse_y]

					collapsList=[]
					for hex in board.spriteGroup.sprites():
						if(hex.rect.collidepoint(point)):
							collapsList.append(hex)
					if(len(collapsList)!=0):
						spriteClck=collapsList[0]
						for hex in collapsList:
							if(spriteClck!=hex):
							#Формула вычисления
							# расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости:
							#AB = √(xb - xa)2 + (yb - ya)2
								x1=spriteClck.rect.centerx
								y1=spriteClck.rect.centery
								x2=hex.rect.centerx
								y2=hex.rect.centery
							
								fromMouse_to_hex=math.sqrt(  (mouse_x-x2)*(mouse_x-x2) + (mouse_y-y2)*(mouse_y-y2) )
								fromMouse_to_spriteClck=math.sqrt(  (mouse_x-x1)*(mouse_x-x1) + (mouse_y-y1)*(mouse_y-y1) )
							
								if(fromMouse_to_spriteClck<=fromMouse_to_hex):
									spriteClck=spriteClck
								elif fromMouse_to_spriteClck>fromMouse_to_hex:
									spriteClck=hex
								
					
					
						if (board.activeHex!=spriteClck) and (not spriteClck.isNPS())and board.activeHex and board.activeHex.isNPS() and ( [spriteClck.index_x,spriteClck.index_y] in 
						board.getNeighborHex(board.activeHex.index_x,board.activeHex.index_y)):

							board.activeHex.needMove(100,0)
							print(id(board.activeHex))
							#spriteClck.setNPS(board.activeHex.np)
							#board.activeHex.np.update()
							#board.activeHex.removeNps()
							detail.firstNps.active=False
						else:
							if board.activeNps:
								if spriteClck.isNPS():
									print("В этом спрайте уже стоит NPS")
								else:
									spriteClck.setNPS(board.activeNps)
									board.activeNps=False
									detail.firstNps.active=False
							else:
								
								board.activeHex=spriteClck
					
							
								listNeighbor=board.getNeighborHex(spriteClck.index_x,spriteClck.index_y)
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

			elif event.button == 3:#right mouse button
				for i in NeighborActiveCell:
						lastHex=i[0]
						lastHex.image=i[1]
				if board.activeHex and board.activeHex.isNPS():
					board.activeHex=False
					detail.firstNps.active=False
						
		elif event.type == pygame.KEYDOWN:
			if( event.key == pygame.K_RIGHT):
				isRightPress=True
			elif event.key == pygame.K_LEFT:
				isLeftPress=True
			elif event.key == pygame.K_DOWN:
				isDownPress=True
			elif event.key == pygame.K_UP:
				isTopPress=True	
		elif event.type == pygame.KEYUP:
			if( event.key == pygame.K_RIGHT):
				isRightPress=False
			elif event.key == pygame.K_LEFT:
				isLeftPress=False
			elif event.key == pygame.K_DOWN:
				isDownPress=False
			elif event.key == pygame.K_UP:
				isTopPress=False
				
		screen.fill(WHITE)	
		board.draw_camera(camera)

	if isLeftPress:
		move=camera.x-camera.moveInOneFPS
		camera.x=max(0,move)
		screen.fill(WHITE)	
		board.draw_camera(camera)				
	if isRightPress: 
		move=camera.x+camera.moveInOneFPS
		camera.x=min(move,1400)
		screen.fill(WHITE)	
		board.draw_camera(camera)
	if isTopPress: 
		move=camera.y-camera.moveInOneFPS
		camera.y=max(0,move)
		screen.fill(WHITE)	
		board.draw_camera(camera)
	if isDownPress: 
		move=camera.y+camera.moveInOneFPS;
		camera.y=min(move,1400)
		screen.fill(WHITE)	
		board.draw_camera(camera)



		
	camera.update()
	detail.draw_all()
	pygame.display.flip()
 

	clock.tick(FPS)

	
	
	
	


Debug=None	