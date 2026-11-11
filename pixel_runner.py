import pygame
import os
from configs import Configs
import game_functions
from obstacle import Obstacle
from player import Player
from score import Score

def run_game():
    pygame.init()
    pygame.display.set_caption('Pixel Runner')
    configs = Configs()
    obstacles = Obstacle(configs)
    player = Player(configs)
    score = Score(configs)
     
    clock = pygame.time.Clock()
    
    print(configs.ground_rect.topright)
    run =  True
    
    while run:
        game_functions.check_events(configs, player, obstacles, score) #inputs
        if configs.game_active:
            player.jump(configs)
            obstacles.obstacle_movement()
            configs.screen.blit(configs.sky_surface,configs.screen_rect.topleft)
            configs.screen.blit(configs.ground_surface,(0,300))
            for obstacle_surface, obstacle_rect in zip(
                obstacles.obstacle_surface_list, obstacles.obstacle_rect_list
            ):
                configs.screen.blit(obstacle_surface, obstacle_rect)
            configs.screen.blit(player.surface_1,player.surface_1_rect)
           
            game_functions.check_player_collide(configs, player, obstacles, score)
            game_functions.desenha_contorno_texto(configs)
            configs.screen.blit(configs.text_surface, (configs.text_rect))
            configs.screen.blit(score.score_txt_surface,(score.rect))
            score.update_score()
            pygame.display.update()
        elif configs.game_over:
            game_functions.game_over(configs,score)
            
        elif not configs.game_over and not configs.game_active:
            game_functions.start_screen(configs, player)

        clock.tick(configs.fps)

run_game()