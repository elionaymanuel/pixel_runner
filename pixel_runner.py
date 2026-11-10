import pygame
import os
from configs import Configs
import game_functions
from snail import Snail
from player import Player

def run_game():
    pygame.init()
    pygame.display.set_caption('Pixel Runner')
    configs = Configs()
    snail = Snail(configs)
    player = Player(configs)
    
    
    clock = pygame.time.Clock()
    
    print(configs.ground_rect.topright)
    run =  True
    while run:
        game_functions.check_events()

        configs.screen.blit(configs.sky_surface,configs.screen_rect.topleft)
        configs.screen.blit(configs.ground_surface,(0,300))
        configs.screen.blit(snail.snail_surface,snail.rect)
        configs.screen.blit(player.player_surface,player.rect)
        game_functions.snail_movement(configs,snail)
        game_functions.player_movement(configs,player)
        game_functions.check_player_collide(configs,player,snail)
        configs.screen.blit(configs.text_surface, (configs.screen_rect.centerx-100,100))
        pygame.display.update()
        clock.tick(configs.fps)

run_game()