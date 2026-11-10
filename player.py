import pygame

class Player():
    def __init__(self,configs):
        self.player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.inicio = configs.screen_width

        #desenha um retangulo ao redor da surface
        self.rect = self.player_surface.get_rect(midbottom = (800,300)) 
     
        #configurações dinamicas
        self.player_velocity = 4
