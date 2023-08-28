import pygame
from EnvironmentalsClass import environmentals

environment = environmentals()

#Creating a class for characters.
class Character:
    def __init__(self, x, y, width, height, color):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.jumpProgressionCount = 10 #Jump speed for our jumping physics formula.
        self.charIsJumping = False 
        self.velocity = 5 #Player movement speed
    
    def update(self):
        #This function is for character movements, animations
        key = pygame.key.get_pressed()
    
        if key[pygame.K_LEFT] and self.x > self.velocity:
            self.x -= self.velocity

        if key[pygame.K_RIGHT] and self.x < environment.getScreenWidth() - self.width - self.velocity:
            self.x += self.velocity
        
        if not (self.charIsJumping): #IF the character is not jumping
            if key[pygame.K_UP] and self.y > self.velocity:
                self.y -= self.velocity 
            
            if key[pygame.K_DOWN] and self.y < environment.getScreenHeight() - self.height - self.velocity:
                self.y += self.velocity

            if key[pygame.K_SPACE]:
                self.charIsJumping = True
    
        else: #Quadratic equation for jumping
            if self.jumpProgressionCount >= -10:
                neg = 1
                if self.jumpProgressionCount < 0:
                    neg = -1
                self.y -= (self.jumpProgressionCount ** 2) * 0.5 * neg
                self.jumpProgressionCount -= 1
            else:
                self.charIsJumping = False
                self.jumpProgressionCount = 10

        #Checking boundaries
        
        if self.x < 0:
            self.x = 0

        if self.x > environment.getScreenWidth() - self.width:
            self.x = environment.getScreenWidth() - self.width
        
        if self.y < 0:
            self.y = 0
        
        if self.y > environment.getScreenHeight() - self.height:
            self.y = environment.getScreenHeight() - self.height
        
        #Updatung the position of the rectangle.
        self.rectangle.x = self.x
        self.rectangle.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)
