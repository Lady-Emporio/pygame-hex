
from MyConst import *
from enum import Enum
import pygame 

class HexType(Enum):
    grass = 1
    woods = 2
    stone = 3
    greenGrown = 4
    lightGreen = 5
    red = 6
    yellow = 7


def getHex(hexType):
	if(hexType==HexType.grass):
		 return Hex(r'image\grass_19.png', hexType)
	elif(hexType==HexType.woods):
		 return Hex(r'image\grass_13.png', hexType)
	elif(hexType==HexType.stone):
		 return Hex(r'image\stone_02.png', hexType)
	elif(hexType==HexType.greenGrown):
		 return Hex(r'image\greenGrown.png', hexType)
	elif(hexType==HexType.lightGreen):
		 return Hex(r'image\lightGreen.png', hexType)
	elif(hexType==HexType.red):
		 return Hex(r'image\red.png', hexType)
	elif(hexType==HexType.yellow):
		 return Hex(r'image\yellow.png', hexType)
	elif type(hexType) != HexType:
		 raise Exception('try create Hex not usual type')
	else:
		raise Exception('try create Hex not do this type create')

	


class Hex(pygame.sprite.Sprite):
	def __init__(self, image, hexType,index_x=None,index_y=None):
		pygame.sprite.Sprite.__init__(self)
		self.hexType = hexType
		
		Simage = pygame.image.load(image)
		self.backgroundImage=pygame.transform.scale(Simage, TILE_SIZE)
		self.image = self.backgroundImage
		self.rect = self.image.get_rect()
		self.index_x=index_x;
		self.index_y=index_y;
		self.surfaceText=None;
		self.listNeighbor=[]
		
		self.np=None
		self.isHaveNps=False

		self.isNeedMove=False
		self.movePointX=0;
		self.movePointY=0;
		self.indexMove=0;

	def isNPS(self):
		return self.isHaveNps;
	def setNPS(self,nps):
		self.np=nps
		self.isHaveNps=True
	def removeNps(self):
		self.np=None
		self.isHaveNps=False
		
	def __repr__(self):
		#return 'Tile(%s)' % self.image
		return 'Hex(%s)' % str(id(self))
	def addSurfeceText(self):
	
		self.removeSurfeceText();
		
		#text=str(self.index_x)+"|"+str(self.index_y)+" - "+str(self.rect.centerx) +"|"+str(self.rect.centery)
		text=str(self.index_x)+"|"+str(self.index_y)
		
		
		SurfaceText=FONT.render(text, False, (255, 255, 255))
		lineX=self.image.get_width()/2-(SurfaceText.get_width()/2)
		lineY=self.image.get_height()/2-(SurfaceText.get_height()/2)
		self.image.blit(SurfaceText, (lineX,lineY))
		
	def removeSurfeceText(self):
		self.image = self.backgroundImage

	def needMove(self,x,y):
		self.isNeedMove=True;
		self.movePointX=x;
		self.movePointY=y;
		self.indexMove=0;

	def goMove(self,rect):
		return rect.move(int(self.movePointX),int(self.movePointY))
		#if self.isNeedMove:
			
			#newrect=pygame.Rect(newrect.left, newrect.top, newrect.width+int(self.movePointX), newrect.height+int(self.movePointY))
			#self.isNeedMove=False;
			#return newrect
		#else:
		return newrect
		
	def endMove(self):
		self.isNeedMove=False
		self.movePointX=0;
		self.movePointY=0;
		self.indexMove=0;

class Layout():
	def __init__(self, display):
		self.display = display;
		self.spriteGroup = pygame.sprite.Group();
		self.hexList=[]
		self.world=None;
		self.initWorld();
		
		self.activeNps=False
		self.activeHex=False
	
	def initWorld(self):
		FIRST_LAYOUT= [
			[
				getHex(HexType.grass), getHex(HexType.woods), getHex(HexType.stone),getHex(HexType.stone),
				getHex(HexType.grass), getHex(HexType.woods), getHex(HexType.stone),getHex(HexType.stone),
			],
			[
				getHex(HexType.greenGrown),getHex(HexType.lightGreen), getHex(HexType.lightGreen),getHex(HexType.red), 
				getHex(HexType.greenGrown),getHex(HexType.lightGreen), getHex(HexType.lightGreen),getHex(HexType.red), 
			],
			[
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.lightGreen), getHex(HexType.red),getHex(HexType.greenGrown), getHex(HexType.greenGrown),
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.greenGrown), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.red),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.yellow), getHex(HexType.red),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.red), getHex(HexType.red),
			],
			[
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.yellow), getHex(HexType.greenGrown),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.greenGrown),getHex(HexType.greenGrown), getHex(HexType.red),
			],
			[
				getHex(HexType.lightGreen), getHex(HexType.yellow),getHex(HexType.greenGrown), getHex(HexType.red),
				getHex(HexType.lightGreen), getHex(HexType.greenGrown),getHex(HexType.greenGrown), getHex(HexType.red),
			],
		]
		
		self.world=FIRST_LAYOUT;
		
		self.hexList=[ [hex for hex in row] for row in self.world ]
		
		y = -1
		x = -1
		for row in self.world:
			x = -1
			y += 1
			for hex in row:
				x+= 1
				hex.index_x=y;#x=y its not error
				hex.index_y=x;#y=x
				self.spriteGroup.add(hex)
								
				if y % 2 == 0:
					hex.rect.x=x * TILE_SIZE[0]
					hex.rect.y=y * TILE_SIZE[1] - (y * DEL_SPACE_BEETWEEN_HEX)

				else:
					hex.rect.x=x * TILE_SIZE[0] + (TILE_SIZE[0] / 2)
					hex.rect.y=y * TILE_SIZE[1] - (y * DEL_SPACE_BEETWEEN_HEX)
				
				hex.addSurfeceText()
				hex.listNeighbor=self.getListIndexNeighborHexFromIndexHex(hex.index_x,hex.index_y)

	def getListIndexNeighborHexFromIndexHex(self,x,y):
		if(x>=len(self.world)):
			return []
		if(y>len(self.world[x])):
			return []
		
		Neighbor=[]
		if(x%2==0):
			leftTop=[x-1,y-1]
			rightTop=[x-1,y]
			leftMiddle=[x,y-1]
			rightMiddle=[x,y+1]
			leftDown=[x+1,y-1]
			rightDown=[x+1,y]
			
			if leftTop[0]>=0 and leftTop[1]>=0:
				Neighbor.append(leftTop)
			
			if rightTop[0]>=0:
				Neighbor.append(rightTop)
			
			if leftMiddle[1]>=0:
				Neighbor.append(leftMiddle)
			
			if rightMiddle[1]<len(self.world[x]):
				Neighbor.append(rightMiddle)
			
			if leftDown[0]<len(self.world) and leftDown[1]>=0:
				Neighbor.append(leftDown)
				
			if rightDown[0]<len(self.world):
				Neighbor.append(rightDown)
			return Neighbor;
		else:
			leftTop=[x-1,y]
			rightTop=[x-1,y+1]
			leftMiddle=[x,y-1]
			rightMiddle=[x,y+1]
			leftDown=[x+1,y]
			rightDown=[x+1,y+1]
			
			if leftTop[0]>=0:
				Neighbor.append(leftTop)
			
			if rightTop[0]>=0 and rightTop[1]<len(self.world[x]):
				Neighbor.append(rightTop)
			
			if leftMiddle[1]>=0:
				Neighbor.append(leftMiddle)
			
			if rightMiddle[1]<len(self.world[x]):
				Neighbor.append(rightMiddle)
			
			if leftDown[0]<len(self.world):
				Neighbor.append(leftDown)
				
			if rightDown[0]<len(self.world) and rightDown[1]<len(self.world[x]):
				Neighbor.append(rightDown)
			return Neighbor;

	def getNeighborHex(self,x,y):
		return self.world[x][y].listNeighbor
			
			
			
	#def draw_world(self):
		
		# y = -1
		# x = -1
		# for row in self.world:
			# x = -1
			# y += 1
			# for hex in row:
				# x += 1
				# if y % 2 == 0:
					# hex.rect.x=x * TILE_SIZE[0]
					# hex.rect.y=y * TILE_SIZE[1] - (y * 20)

				# else:
					# hex.rect.x=x * TILE_SIZE[0] + (TILE_SIZE[0] / 2)
					# hex.rect.y=y * TILE_SIZE[1] - (y * 20)
					
				# SurfaceText = hex.getSurfeceText();
				# lineX=hex.rect.x+ (TILE_SIZE[0] / 2)-(SurfaceText.get_width()/2)
				# lineY=hex.rect.y+ (TILE_SIZE[0] / 2)#-(SurfaceText.get_height()/2)
				# self.display.blit(hex.image, hex.rect)
				# self.display.blit(SurfaceText, (lineX, lineY))
		#self.spriteGroup.draw(self.display)

	def draw_camera(self,camera):
		lastSprite=[]
		for sprite in self.spriteGroup:
			self.display.blit(sprite.backgroundImage, camera.apply(sprite))
			self.display.blit(sprite.image, camera.apply(sprite))
			if(sprite.isNPS()):
				lastSprite.append(sprite)
				
		for sprite in lastSprite:
			#self.display.blit(sprite.np.image, camera.apply(sprite).move(int(TILE_SIZE[0]/4),int(TILE_SIZE[1]/4)) )
					oldRect=camera.apply(sprite).move(int(TILE_SIZE[0]/4),int(TILE_SIZE[1]/4)) ;
					rect=sprite.goMove(oldRect )
					print(sprite)
					print(oldRect)
					print(rect)
					self.display.blit(sprite.np.image,rect)
	