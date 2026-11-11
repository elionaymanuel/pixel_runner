import pygame

class Player():
    def __init__(self,configs):

        ###imagem1
        self.surface_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.surface_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [self.surface_1,self.surface_2]
        #desenha um retangulo ao redor da surface
        self.surface_1_rect = self.surface_1.get_rect(midbottom = (80,configs.ground_superficie)) 

        ### stand
        self.stand_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
        self.stand_surface = pygame.transform.scale2x(self.stand_surface)
        #self.stand_surface = pygame.transform.rotozoom(self.stand_surface,90,1)
        self.stand_rect = self.stand_surface.get_rect(center = configs.screen_rect.center)
        #self.inicio = configs.screen_width

        
        
        #configurações dinamicas
        self.player_velocity = 4
        self.gravity = 0
        self.vertical_speed = 0
        self.on_ground = True

    def player_movement (self, configs):
        if self.surface_1_rect.left>=configs.screen_rect.right:
            self.surface_1_rect.left+=self.player_velocity
        else:
            self.surface_1_rect.left = 0
            self.surface_1_rect.left-=self.player_velocity

    def jump(self, configs):
        self.surface_1_rect.y += self.gravity
        self.gravity += configs.gravity

        if self.surface_1_rect.bottom >= configs.ground_superficie:
            self.surface_1_rect.bottom = configs.ground_superficie
            self.gravity = 0
            self.on_ground = True
        

