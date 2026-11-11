import pygame
from random import randint


class Obstacle:
    def __init__(self,configs):
        self.snail_frames = [
            pygame.image.load("graphics/snail/snail1.png").convert_alpha(),
            pygame.image.load("graphics/snail/snail2.png").convert_alpha(),
        ]
        self.fly_frames = [
            pygame.image.load("graphics/Fly/Fly1.png").convert_alpha(),
            pygame.image.load("graphics/Fly/Fly2.png").convert_alpha(),
        ]
        self.obstacle_velocity = 4
        self.obstacle_list = []

    def spawn_obstacle(self):
        """Escolhe e adiciona uma lesma ou mosca com sua animação."""
        obstacle_choice = randint(0, 2)

        if obstacle_choice == 0:
            obstacle_frames = self.snail_frames
            ground_height = 300
        else:
            obstacle_frames = self.fly_frames
            ground_height = 210

        obstacle_rect = obstacle_frames[0].get_rect(
            bottomright=(randint(900, 1100), ground_height)
        )
        self.obstacle_list.append((obstacle_frames, obstacle_rect, 0.0))

    def obstacle_movement(self):
        remaining_obstacles = []

        for obstacle_frames, obstacle_rect, animation_index in self.obstacle_list:
            obstacle_rect.x -= self.obstacle_velocity
            animation_index = (
                animation_index + 0.1
            ) % len(obstacle_frames)

            if obstacle_rect.right > -100:
                remaining_obstacles.append(
                    (obstacle_frames, obstacle_rect, animation_index)
                )

        self.obstacle_list = remaining_obstacles

    def draw(self, screen):
        for obstacle_frames, obstacle_rect, animation_index in self.obstacle_list:
            current_frame = obstacle_frames[int(animation_index)]
            screen.blit(current_frame, obstacle_rect)