import pygame

class Score():
    def __init__(self,configs):
        self.score_txt = pygame.font.Font("font/Pixeltype.ttf",50)
        #recebe 3 argumentos, string, anti alising e a cor
        self.score_value = 0
        self.start_ticks = pygame.time.get_ticks()
        self.score_txt_surface = self.score_txt.render(f'{self.score_value}',False, (64,64,64))
        self.rect = self.score_txt_surface.get_rect(
            topright=(configs.screen_rect.right - 20, configs.screen_rect.top + 20)
)
    def update_score(self):
        new_score = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if new_score == self.score_value:
            return self.score_value

        previous_topright = self.rect.topright
        self.score_value = new_score
        self.score_txt_surface = self.score_txt.render(
            str(self.score_value), False, (64,64,64)
        )
        self.rect = self.score_txt_surface.get_rect(topright=previous_topright)
        return self.score_value

    def reset_score(self):
        previous_topright = self.rect.topright
        self.score_value = 0
        self.start_ticks = pygame.time.get_ticks()
        self.score_txt_surface = self.score_txt.render(
            str(self.score_value), False, (64,64,64)
        )
        self.rect = self.score_txt_surface.get_rect(topright=previous_topright)

    def count_score(self):
        pygame.time.get_ticks()
        #print(pygame.time.get_ticks())