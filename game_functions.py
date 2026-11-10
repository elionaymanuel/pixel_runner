import pygame
#import sys
import os
from configs import Configs

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            #pygame.quit()
            #sys.exit()
            os._exit(0)
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print ('click! do mouse')

            
    return True    

def check_KEYDOWN_events(event):
    
    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        os._exit(0)
        

def snail_movement (configs,snail):
    if snail.rect.left>=-50:
        snail.rect.left-=snail.snail_velocity
    else:
        snail.rect.left = configs.screen_width
        snail.rect.left+=snail.snail_velocity

def player_movement (configs,player):
    if player.rect.left>=configs.screen_rect.right:
        player.rect.left+=player.player_velocity
    else:
        player.rect.left = 0
        player.rect.left-=player.player_velocity

def check_player_collide(configs,player,snail):
    if player.rect.colliderect(snail.rect):
        snail.rect.left = configs.screen_width