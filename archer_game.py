import pygame
import sys
from time import sleep

BURLYWOOD = (222,184,135)
GOLD = (255,215,0)
WHITE = (255,255,255)
SILVER = (192,192,192)
BLACK = (0,0,0)
posx = 100
posy = 100
def draw_arrow(posx, posy):
    pygame.draw.rect(screen, BLACK, (posx,posy-20,-60,40),1)    
    pygame.draw.line(screen, BURLYWOOD, (posx,posy), (posx-50,posy), 2)
    pygame.draw.rect(screen, BLACK, (posx,posy-20,-60,40),1)   
    pygame.draw.line(screen, SILVER, (posx,posy), (posx-10,posy-5), 2)
    pygame.draw.rect(screen, BLACK, (posx,posy-20,-60,40),1)   
    pygame.draw.line(screen, SILVER, (posx,posy), (posx-10,posy+5), 2)
    pygame.draw.rect(screen, BLACK, (posx,posy-20,-60,40),1)   
    for x in range(0,10,2):
        pygame.draw.rect(screen, BLACK, (posx,posy-20,-60,40),1)   
        pygame.draw.line(screen, WHITE, (posx-50+x,posy), (posx+x-50-7,posy-5), 2)
        pygame.draw.line(screen, WHITE, (posx-50+x,posy), (posx+x-50-7,posy+5), 2)
    pygame.display.update()

def arrow_release(posx, current_posy):
    for r in range (posx,width+60,1):
        draw_arrow(r, current_posy)
        pygame.time.wait(1)

game_over = False

pygame.init()
width = 800
height = 500
screen_size = (width, height)


screen = pygame.display.set_mode(screen_size)

pygame.display.update()

while not game_over:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEMOTION:
            posy = event.pos[1]
   
            draw_arrow(posx, int(posy))
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_posy = event.pos[1]
            arrow_release(posx, current_posy)
