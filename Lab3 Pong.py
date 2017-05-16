# Yunshu Zhao and Etienne Asselin
# 2015 Fall Term
# University of Alberta

import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()
   pygame.font.init()

   surfaceSize = (500, 400)
   windowTitle = 'Pong'
   frameDelay = 0.02

   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   paddle1 = [50,160,10,80]
   paddle2 = [440,160,10,80]
   bRadius = 10
   bCenter = [250, 200]
   bSpeed = [8, 2]
   score = [0, 0]

   pygame.display.update()

   while True:
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
      if max(score)<11:
         moveBall(bCenter, bSpeed, bRadius, score, surface)
         movePaddle(paddle1, paddle2)
         collision(bCenter, bSpeed, bRadius, paddle1, paddle2)      
         gameOver = update(bCenter, bRadius, paddle1, paddle2, score, surface)
         
         pygame.display.update()

      time.sleep(frameDelay)

def update(bCenter, bRadius, paddle1, paddle2, score, surface):

   surface.fill(pygame.Color('black'))
   pygame.draw.circle(surface, pygame.Color('white'), bCenter, bRadius , 0)
   pygame.draw.rect(surface, pygame.Color('white'), paddle1, 0)
   pygame.draw.rect(surface, pygame.Color('white'), paddle2, 0)
   tempsurface=pygame.font.SysFont(None,72).render(str(score[0]), 1, pygame.Color('white'))
   surface.blit(tempsurface, (0, 0), None, 0)
   tempsurface=pygame.font.SysFont(None,72).render(str(score[1]), 1, pygame.Color('white'))
   tempsize = tempsurface.get_size()
   size = surface.get_size()
   surface.blit(tempsurface, (size[0]-tempsize[0], 0), None, 0)
   
   return False

def moveBall(bCenter, bSpeed, bRadius, score, surface):
   size = surface.get_size()
   for axis in range(0,2):
      bCenter[axis] = bCenter[axis] + bSpeed[axis]
      if bCenter[axis] < bRadius:
         bSpeed[axis] = -bSpeed[axis]
         score[1]+=abs(axis-1)
      if bCenter[axis] + bRadius > size[axis]:
         bSpeed[axis] = -bSpeed[axis]
         score[0]+=abs(axis-1)

def movePaddle(paddle1, paddle2):
   keys = pygame.key.get_pressed()
   paddle1[1]=max(0,paddle1[1]-3*keys[K_q])
   paddle1[1]=min(400-paddle1[3],paddle1[1]+3*keys[K_a])
   paddle2[1]=max(0,paddle2[1]-3*keys[K_p])
   paddle2[1]=min(400-paddle2[3],paddle2[1]+3*keys[K_l])
         
def collision(bCenter, bSpeed, bRadius, paddle1, paddle2):
   if bSpeed[0]<0:
      if bCenter[1]>=paddle1[1] and bCenter[1]<=paddle1[1]+paddle1[3]:
         if bCenter[0]-bRadius<=paddle1[0]+paddle1[2]:
            bSpeed[0] = -bSpeed[0]

   else:
      if bCenter[1]>=paddle2[1] and bCenter[1]<=paddle2[1]+paddle2[3]:
         if bCenter[0]+bRadius>=paddle2[0]:
            bSpeed[0] = -bSpeed[0]  

main()
