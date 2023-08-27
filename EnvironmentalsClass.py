import pygame
import os

pygame.init()

#Function for our system environmentals
class environmentals:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        info = pygame.display.Info() #getting info about our system.
        self.screenWidth, self.screenHeight = info.current_w, info.current_h #assigning the screen info to variables;
        self.screen = pygame.display.set_mode((self.screenWidth - 100, self.screenHeight - 100), pygame.RESIZABLE) #Screen size based on the OS and game is resizable.
        self.clock = pygame.time.Clock()
        
    def getScreenWidth(self):
        return self.screenWidth

    def getScreenHeight(self):
        return self.screenHeight