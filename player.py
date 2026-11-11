import pygame

class Player():
    def __init__(self,configs):

        ###imagem1
        walk_surface_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        walk_surface_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [walk_surface_1, walk_surface_2]
        self.player_index = 0
        self.jump_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        #desenha um retangulo ao redor da surface
        self.current_surface = self.player_walk[self.player_index]
        self.current_rect = self.current_surface.get_rect(
            midbottom=(80, configs.ground_superficie)
        )

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
        if self.current_rect.left>=configs.screen_rect.right:
            self.current_rect.left+=self.player_velocity
        else:
            self.current_rect.left = 0
            self.current_rect.left-=self.player_velocity

    def jump(self, configs):
        self.current_rect.y += self.gravity
        self.gravity += configs.gravity

        if self.current_rect.bottom >= configs.ground_superficie:
            self.current_rect.bottom = configs.ground_superficie
            self.gravity = 0
            self.on_ground = True

    def player_animation (self):
        if not self.on_ground:
            self.current_surface = self.jump_surface
        else:
            self.player_index = (
                self.player_index + 0.1
            ) % len(self.player_walk)
            self.current_surface = self.player_walk[int(self.player_index)]

        midbottom = self.current_rect.midbottom
        self.current_rect = self.current_surface.get_rect(midbottom=midbottom)
            
