import pygame
from EnvironmentalsClass import environmentals

environment = environmentals()

#Creating a class for characters.
class Character:
    def __init__(self, x, y, width, height, color):
        self.rectangle = pygame.Rect(100, 100, 75, 75)
        self.color = color
    
    def update(self):
        #This function is for character movements, animations
        key = pygame.key.get_pressed()
        velocity = 5
    
        if key[pygame.K_UP]:
            self.rectangle.y -= velocity 
    
        if key[pygame.K_DOWN]:
            self.rectangle.y += velocity

        if key[pygame.K_LEFT]:
            self.rectangle.x -= velocity

        if key[pygame.K_RIGHT]:
            self.rectangle.x += velocity
        
        if self.rectangle.left < 0:
            self.rectangle.left = 0

        if self.rectangle.right > environment.getScreenWidth():
            self.rectangle.right = environment.getScreenWidth()
        
        if self.rectangle.top < 0:
            self.rectangle.top = 0
        
        if self.rectangle.bottom > environment.getScreenHeight():
            self.rectangle.bottom = environment.getScreenHeight() 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)