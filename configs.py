import pygame
class Configs:
    def __init__(self):
        ###Configurações ESTATICAS
        self.screen_width = 800
        self.screen_height = 400
        self.fps = 60
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.screen.fill('White')
        self.screen_rect = self.screen.get_rect()
        #imagens (chao e ceu)
        self.sky_surface = pygame.image.load("graphics/Sky.png").convert()
        self.ground_surface = pygame.image.load("graphics/ground.png").convert()
        self.ground_superficie = 300
        self.gravity = 1
        self.ground_rect = self.ground_surface.get_rect(bottomleft=self.screen_rect.bottomleft)
        #textos
        #self.test_font = pygame.font.Font(None,50)
        self.test_font = pygame.font.Font("font/Pixeltype.ttf",50)
        #recebe 3 argumentos, string, anti alising e a cor
        self.text_surface = self.test_font.render('pixel runner',False, (64,64,64))
        self.text_rect = self.text_surface.get_rect(center = (self.screen_rect.centerx,50))

        self.game_active = True
        self.game_over = pygame.font.Font("font/Pixeltype.ttf",80)
        self.game_over_surface = self.game_over.render('GAME OVER',False, (64,64,64))
        self.game_over_rect = self.game_over_surface.get_rect(center = (self.screen_rect.centerx,self.screen_rect.centery))

        

    
        
        
        
