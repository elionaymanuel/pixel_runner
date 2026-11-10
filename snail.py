import pygame


class Snail():
    def __init__(self,configs):
        self.snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
        #self.inicio= configs.ground_rect.topright[0]
        #a snail começa fora da tela
        self.rect = self.snail_surface.get_rect(midbottom = (configs.screen_width + 36, 300))
        
        #configurações dinamicas
        self.snail_velocity = 4