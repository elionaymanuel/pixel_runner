import pygame
#import sys
import os

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            #pygame.quit()
            #sys.exit()
            os._exit(0)
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event)

            
    return True    

def check_KEYDOWN_events(event):
    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        os._exit(0)
