# Yunshu Zhao and Etienne Asselin
# 2015 Fall Term
# University of Alberta

import pygame, sys, random
from pygame.locals import *
pygame.init()

# User-defined classes

# Tile object class
class Tile:
   
   #Initialize graphic related variables
   borderWidth = 3 # the pixel width of the tile border

   #Initialize the object and assign a image
   def __init__(self, x, y, tilelist, surface):
      self.content = tilelist[-1]
      del tilelist[-1]
      self.rect = self.content.get_rect()
      self.rect[0] = x
      self.rect[1] = y
      self.surface = surface
      self.state = 0 #0 is hidden 1 is revealed
           
   #For drawing the tile
   def draw(self, hiddenimage):
      if self.state:
         self.surface.blit(self.content, self.rect)
      else:
         self.surface.blit(hiddenimage, self.rect)

class MEM:

   boardSize = 4
   clicks = 0
   clock = 0
   tick = 1
   currentclick = 0
   cooldown = 0
   
   #Initialize the game
   def __init__(self, surface):
      #Load bitmaps, assign to a list, randomize
      self.hiddenimage = pygame.image.load("image0.bmp") 
      
      self.tilelist=[]
      for i in range(0,8):
         imagefiletemp = pygame.image.load("image"+str(i+1)+".bmp") 
         self.tilelist.extend([imagefiletemp,imagefiletemp])
      random.shuffle(self.tilelist)
      
      self.mousestate = 0 #0 for up 1 for down
      self.clickedtile = [None, None] #0 is downclick, 1 is release
      self.click = [None, None] #Overturned tiles
      
      #Create Tiles into list board
      self.surface = surface
      self.board = []
      for rowIndex in range(0,MEM.boardSize):
         row = []
         for columnIndex in range(0,MEM.boardSize):
            side = self.surface.get_height() // MEM.boardSize
            x = columnIndex*side + Tile.borderWidth
            y = rowIndex*side + Tile.borderWidth
            tile = Tile(x, y, self.tilelist, self.surface)
            row.append(tile)
         self.board.append(row)   
   
   #Draw tiles in board
   def draw(self, surface):
      for row in self.board:
         for tile in row:
            tile.draw(self.hiddenimage)
      MEM.clock+=(pygame.time.get_ticks()//1000-MEM.clock)*MEM.tick
      tempsurface=pygame.font.SysFont(None,72).render(str(MEM.clock), 1, pygame.Color('white'), pygame.Color('black'))
      tempsize = tempsurface.get_size()
      size = surface.get_size()
      pygame.draw.rect(surface, pygame.Color('black'), [415, 0, 85, 100])
      surface.blit(tempsurface, (size[0]-tempsize[0], 0), None, 0)      
      
   def checkclick(self):
      if pygame.mouse.get_pressed()[0] != self.mousestate: #Compare current and previous state, check for change
         self.mousestate = not self.mousestate #Record new state
         
         side = self.hiddenimage.get_height()
         for rowIndex in range(0,MEM.boardSize):
            for columnIndex in range(0,MEM.boardSize):
               currenttile = self.board[rowIndex][columnIndex]
               if currenttile.rect[0]<=pygame.mouse.get_pos()[0]<=currenttile.rect[0]+side:
                  if currenttile.rect[1]<=pygame.mouse.get_pos()[1]<=currenttile.rect[1]+side:
                     self.clickedtile[not self.mousestate]=currenttile
                     break
            else:
               continue
            break
         if self.mousestate == 0 and self.clickedtile[0] != None:
            if self.clickedtile[0] == self.clickedtile[1]: #If the click and release happened on the same tile
               self.clickedtile[0].state = 1
               self.click[MEM.currentclick] = self.clickedtile[0]
               if MEM.currentclick == 1:
                  if self.click[0] != self.click[1]:
                     MEM.currentclick = 0
                     if self.click[0].content == self.click[1].content:
                        self.click[0] = None
                        self.click[1] = None
                        MEM.clicks += 1
                        if MEM.clicks == 8:#Stop the clock at 16 points
                           MEM.tick = 0                        
                     else:
                        MEM.cooldown = 1000
               else:
                  MEM.currentclick = 1

   def update(self, surface):
      if MEM.cooldown>=1:
         MEM.cooldown-=1
         if MEM.cooldown == 0:
            MEM.currentclick = 0
            self.click[0].state = 0
            self.click[1].state = 0
      if MEM.cooldown == 0:
         self.checkclick()
      self.draw(surface)   

# User-defined functions

def main():

   surfaceSize = (500, 415)
   windowTitle = 'Memory'

   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   gameOver = False
   mem = MEM(surface)

   # Draw objects
   mem.draw(surface)

   # Refresh the display
   pygame.display.update()

   # Loop forever
   while True:
      # Handle events
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
      # Update and draw objects for the next frame
      mem.update(surface)

      # Refresh the display
      pygame.display.update()

main()

