import pygame
#import sys
import os
from configs import Configs
from random import randint

def check_events(configs, player, obstacles, score):
    """Processa eventos de janela, teclado e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            #pygame.quit()
            #sys.exit()
            os._exit(0)
        elif event.type == pygame.USEREVENT + 1 and configs.game_active:
            respaw_enemys(obstacles)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                os._exit(0)
            if configs.game_over:
                configs.game_over = False
            elif not configs.game_active:
                start_new_game(configs, player, obstacles, score)
            elif event.key == pygame.K_SPACE:
                start_jump(player)
        elif event.type == pygame.KEYUP:
            check_KEYUP_events(event,player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if configs.game_over:
                configs.game_over = False
            elif not configs.game_active:
                start_new_game(configs, player, obstacles, score)
            else:
                start_jump(player)
            
    return True    

def start_jump(player):
    """Inicia o pulo do jogador se ele estiver no chão."""
    if player.on_ground:
        player.gravity = -20
        player.on_ground = False


def start_new_game(configs, player, obstacles, score):
    """Reinicia jogador, inimigos e pontuação para uma nova partida."""
    player.surface_1_rect.midbottom = (80, configs.ground_superficie)
    player.gravity = 0
    player.on_ground = True
    obstacles.obstacle_rect_list.clear()
    obstacles.obstacle_surface_list.clear()
    score.reset_score()
    configs.game_over = False
    configs.game_active = True
    timer()

def check_KEYUP_events(event,player):
        """Trata a soltura de teclas; atualmente informa quando Espaço é solto."""
        if  event.key == pygame.K_SPACE:
            print('key space up')


def check_player_collide(configs, player, obstacles, score):
    """Encerra a partida quando o jogador colide com algum obstáculo."""
    if any(
        player.surface_1_rect.colliderect(rect)
        for rect in obstacles.obstacle_rect_list
    ):
        pygame.time.set_timer(pygame.USEREVENT + 1, 0)
        #score.score_value+=1
        #score.update_score()
        configs.game_active = False
        configs.game_over = True
  


def desenha_contorno_texto(configs):
        """Desenha o fundo retangular atrás do texto da tela."""
        pygame.draw.rect(configs.screen,'#c0e8ec',configs.text_rect)#preenchimento
        #pygame.draw.rect(configs.screen,'Black',configs.text_rect,1,2)#borda

def game_over(configs,score):
    """Desenha a tela de fim de jogo e mostra a pontuação final."""
    configs.screen.fill(configs.cor_inicio)
    configs.screen.blit(configs.sky_surface,configs.screen_rect.topleft)
    configs.screen.blit(configs.ground_surface,(0,300))
    configs.screen.blit(configs.game_over_surface, (configs.game_over_surface.get_rect(center = (configs.screen_rect.centerx,configs.screen_rect.centery))))
    score_message = configs.test_font.render(f'seu score: {score.score_value}',False,(111,196,169))
    score_message_rect = score_message.get_rect(
        midtop=(configs.game_over_rect.centerx, configs.game_over_rect.bottom + 10)
    )
    configs.screen.blit(score_message,score_message_rect)
    pygame.display.update()


def timer():
    """Configura o evento periódico que cria novos obstáculos."""
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer,1400)

def start_screen(configs, player):
    """Desenha a tela inicial com o título, o jogador e a mensagem."""
    configs.screen.fill(configs.cor_inicio)
    configs.screen.blit(configs.text_surface, (configs.text_rect))
    
    configs.screen.blit(player.stand_surface, player.stand_rect)

    configs.game_message_rect.midtop = (
        player.stand_rect.centerx,
        player.stand_rect.bottom + 10
    )

    configs.screen.blit(configs.game_message,configs.game_message_rect)
    pygame.display.update()

def respaw_enemys(obstacles):
    """Cria um obstáculo fora da tela à direita e o adiciona à lista."""
    if randint(0,2):
        obstacle_surface = obstacles.snail_surface
        ground_height = 300
    else:
        obstacle_surface = obstacles.fly_surface
        ground_height = 210

    obstacle_rect = obstacle_surface.get_rect(
        bottomright=(randint(900, 1100), ground_height)
    )
    obstacles.obstacle_rect_list.append(obstacle_rect)
    obstacles.obstacle_surface_list.append(obstacle_surface)
     