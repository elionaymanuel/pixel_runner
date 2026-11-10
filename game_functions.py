import pygame
#import sys
import os
from configs import Configs

def check_events(configs,player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            #pygame.quit()
            #sys.exit()
            os._exit(0)
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event,player)
            configs.game_active = True
        elif event.type == pygame.KEYUP:
            check_KEYUP_events(event,player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            jump(configs, player)
            configs.game_active = True

    return True    

def jump(configs, player):
    player.rect.y += player.gravity
    player.gravity += configs.gravity

    if player.rect.bottom >= configs.ground_superficie:
        player.rect.bottom = configs.ground_superficie
        player.gravity = 0
        player.on_ground = True

def check_KEYDOWN_events(event,player):
    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        os._exit(0)
    if event.key == pygame.K_SPACE and player.on_ground:
        player.gravity = -20
        player.on_ground = False

def check_KEYUP_events(event,player):
        if  event.key == pygame.K_SPACE:
            print('key space up')

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

def check_player_collide(configs,player,snail,score):
    if player.rect.colliderect(snail.rect):
        snail.rect.left = configs.screen_width
        #score.score_value+=1
        #score.update_score()
        configs.game_active = False
    


def desenha_contorno_texto(configs):
        pygame.draw.rect(configs.screen,'#c0e8ec',configs.text_rect)#preenchimento
        #pygame.draw.rect(configs.screen,'Black',configs.text_rect,1,2)#borda

def game_over(configs):
    configs.screen.fill('White')
    
    configs.screen.blit(configs.sky_surface,configs.screen_rect.topleft)
    configs.screen.blit(configs.ground_surface,(0,300))
    configs.screen.blit(configs.game_over_surface, (configs.game_over_surface.get_rect(center = (configs.screen_rect.centerx,configs.screen_rect.centery))))
        
    pygame.display.update()