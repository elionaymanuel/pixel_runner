import pygame
import os
from configs import Configs
import game_functions


def run_game():
    pygame.init()
    configs = Configs()
    pygame.display.set_caption('Pixel Runner')
    screen = pygame.display.set_mode((configs.screen_width, configs.screen_height))
    screen.fill('White')
    screen_rect = screen.get_rect()
    sky_surface = pygame.image.load("graphics/Sky.png")
    ground_surface = pygame.image.load("graphics/ground.png")
    ground_rect = ground_surface.get_rect(bottomleft=screen_rect.bottomleft)
    clock = pygame.time.Clock()
    print(screen.get_rect())
    print(screen_rect.topleft)
    print(screen_rect.bottomleft)
    run =  True
    while run:
        run = game_functions.check_events()

        screen.blit(sky_surface,screen_rect.topleft)
        screen.blit(ground_surface,ground_rect)
        pygame.display.update()
        clock.tick(configs.fps)

run_game()