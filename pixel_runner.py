import pygame
import os
from configs import Configs
import game_functions
from snail import Snail
from player import Player
from score import Score

def run_game():
    pygame.init()
    pygame.display.set_caption('Pixel Runner')
    configs = Configs()
    snail = Snail(configs)
    player = Player(configs)
    score = Score(configs)
    
    
    
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
        configs.desenha_contorno_texto()
        configs.screen.blit(configs.text_surface, (configs.text_rect))
        configs.screen.blit(score.score_txt_surface,(score.rect))
        pygame.display.update()
        clock.tick(configs.fps)

run_game()