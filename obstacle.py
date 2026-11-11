import pygame


class Obstacle:
    def __init__(self,configs):
        self.snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha() #lesma
        self.fly_surface = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha() #mosca
        self.obstacle_velocity = 4
        self.obstacle_rect_list = []
        self.obstacle_surface_list = []

    def obstacle_movement(self):
        remaining_obstacle_rects = []
        remaining_obstacle_surfaces = []

        for obstacle_surface, obstacle_rect in zip(
            self.obstacle_surface_list, self.obstacle_rect_list
        ):
            obstacle_rect.x -= self.obstacle_velocity

            if obstacle_rect.right > -100:
                remaining_obstacle_rects.append(obstacle_rect)
                remaining_obstacle_surfaces.append(obstacle_surface)

        self.obstacle_rect_list = remaining_obstacle_rects
        self.obstacle_surface_list = remaining_obstacle_surfaces