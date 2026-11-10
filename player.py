import pygame

class Player():
    def __init__(self,configs):
        self.player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        #self.inicio = configs.screen_width

        #desenha um retangulo ao redor da surface
        self.rect = self.player_surface.get_rect(midbottom = (80,configs.ground_superficie)) 
        
        #configurações dinamicas
        self.player_velocity = 4
        self.gravity = 0
        self.vertical_speed = 0
        self.on_ground = True
        

