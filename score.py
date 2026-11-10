import pygame

class Score():
    def __init__(self,configs):
        self.score_txt = pygame.font.Font("font/Pixeltype.ttf",50)
        #recebe 3 argumentos, string, anti alising e a cor
        self.score = 0
        self.score_txt_surface = self.score_txt.render(f'{self.score}',False, 'Black')
        self.rect = self.score_txt_surface.get_rect(
            topright=(configs.screen_rect.right - 20, configs.screen_rect.top + 20)
)