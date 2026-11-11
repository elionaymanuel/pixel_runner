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
    
    while run:  # Mantém o jogo rodando enquanto run for verdadeiro.
        # Lê e processa eventos de teclado, mouse e janela.
        game_functions.check_events(configs, player, obstacles, score)
        if configs.game_active:  # Atualiza e desenha a partida em andamento.
            player.jump(configs)  # Atualiza a posição vertical do jogador.
            player.player_animation()  # Escolhe o sprite adequado para o jogador.
            obstacles.obstacle_movement()  # Move e remove obstáculos que saíram da tela.
            # Desenha o céu como fundo da cena.
            configs.screen.blit(configs.sky_surface, configs.screen_rect.topleft)
            # Desenha o chão na tela.
            configs.screen.blit(configs.ground_surface, (0, 300))
            obstacles.draw(configs.screen)  # Desenha todos os obstáculos ativos.
            # Desenha o sprite atual do jogador na posição atual.
            configs.screen.blit(player.current_surface, player.current_rect)
            # Verifica se o jogador colidiu com algum obstáculo.
            game_functions.check_player_collide(configs, player, obstacles, score)
            # Desenha o fundo retangular atrás do texto do jogo.
            game_functions.desenha_contorno_texto(configs)
            # Desenha o título do jogo.
            configs.screen.blit(configs.text_surface, configs.text_rect)
            # Desenha a pontuação na tela.
            configs.screen.blit(score.score_txt_surface, score.rect)
            score.update_score()  # Atualiza o valor da pontuação pelo tempo decorrido.
            pygame.display.update()  # Exibe na janela os desenhos deste quadro.
        elif configs.game_over:  # Se a partida terminou, mostra a tela de fim.
            game_functions.game_over(configs, score)
        elif not configs.game_over and not configs.game_active:  # Se não começou, mostra a tela inicial.
            game_functions.start_screen(configs, player)
        # Limita a velocidade do loop à quantidade de quadros por segundo configurada.
        clock.tick(configs.fps)

run_game()