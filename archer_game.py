import pygame
import sys


BURLYWOOD = (222,184,135)
GOLD = (255,215,0)
WHITE = (255,255,255)
SILVER = (192,192,192)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED_LIGHT = (255,77,77)
BLUE_LIGHT = (51,204,255)
BACKGROUND_COLOR = (0,0,0)
SHIELD_HEIGHT = 80
ARROW_SPEED = 3
SHIELD_SPEED = 3
posx = 100
posy = 100
turn_direction = 0

def draw_arrow(posx, posy):

    pygame.draw.line(screen, BURLYWOOD, (posx,posy), (posx-50,posy), 2)
    pygame.draw.line(screen, SILVER, (posx,posy), (posx-10,posy-5), 2)
    pygame.draw.line(screen, SILVER, (posx,posy), (posx-10,posy+5), 2)
    for x in range(0,10,2):
        pygame.draw.line(screen, WHITE, (posx-50+x,posy), (posx+x-50-7,posy-5), 2)
        pygame.draw.line(screen, WHITE, (posx-50+x,posy), (posx+x-50-7,posy+5), 2)
    pygame.display.update()
    #clear last arrow position
    pygame.draw.line(screen, BACKGROUND_COLOR, (posx,posy), (posx-50,posy), 2)
    pygame.draw.line(screen, BACKGROUND_COLOR, (posx,posy), (posx-10,posy-5), 2)
    pygame.draw.line(screen, BACKGROUND_COLOR, (posx,posy), (posx-10,posy+5), 2)
    for x in range(0,10,2):
        pygame.draw.line(screen, BACKGROUND_COLOR, (posx-50+x,posy), (posx+x-50-7,posy-5), 2)
        pygame.draw.line(screen, BACKGROUND_COLOR, (posx-50+x,posy), (posx+x-50-7,posy+5), 2)

def arrow_release(posx, posy):
    # for r in range (posx,width+60,1):
    #     draw_arrow(r, current_posy)
    #     pygame.time.wait(2)
    while posx <= (width+61):
        draw_arrow(posx, posy)
        posx +=1
        pygame.time.wait(ARROW_SPEED)

def draw_shield(shield_posy):
    pygame.draw.rect(screen, WHITE, (width-60, shield_posy, 20,SHIELD_HEIGHT), 0) #0 width is filling object
    pygame.draw.rect(screen, BLUE_LIGHT, (width-60, shield_posy+10, 15, SHIELD_HEIGHT-20), 0)
    pygame.draw.rect(screen, RED_LIGHT, (width-60, shield_posy+20, 10, SHIELD_HEIGHT-40), 0)
    pygame.draw.rect(screen, YELLOW, (width-60, shield_posy+30, 5, SHIELD_HEIGHT-60), 0)
    # pygame.display.update()
    # pygame.draw.rect(screen, BACKGROUND_COLOR, (width-60, shield_posy, 20,SHIELD_HEIGHT), 0)

def shield_move():
    shield_posy = 0
    turn_direction = 0
    while(True):
        if turn_direction == 0:
            while shield_posy+SHIELD_HEIGHT <= height:
                draw_shield(shield_posy)
                shield_posy +=1
                #pygame.time.wait(SHIELD_SPEED)
            turn_direction = 1
        else:
            while shield_posy >= height:
                draw_shield(shield_posy)
                shield_posy -=1
                pygame.time.wait(SHIELD_SPEED)
            turn_direction = 0

game_over = False

pygame.init()
pygame.display.set_caption("Archer")



width = 800
height = 500
screen_size = (width, height)


screen = pygame.display.set_mode(screen_size)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEMOTION:
            posy = event.pos[1]
            posx = event.pos[0]
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            posy = event.pos[1]
            arrow_release(posx, posy)
    
        draw_shield(109)
        draw_arrow(posx, posy)

    screen.fill(BACKGROUND_COLOR)
    # pygame.display.update()
    #shield_move()

   