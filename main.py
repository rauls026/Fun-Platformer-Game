#This project is creating a 2D game using pygame.
import pygame
from CharacterClass import Character
from EnvironmentalsClass import environmentals


environment = environmentals()
character1 = Character(300, 600, 64, 64, 'blue') #Creating a character based on our Character class.

#Setting up the pygame
pygame.init()

def updateGamewindow():
    #Graphics are being rendered here
    #environment.screen.blit()
    environment.screen.fill((255, 255, 255))
    character1.draw(environment.screen)
    character1.update() #Calling the update function for player movement.


def main():
   
#This is a while loop for the game.
    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If the X button is pressed to close the window, the game will close
                running = False


        updateGamewindow()
        pygame.display.flip() #refreshing the display
        pygame.display.set_caption("Raul's Fun Platformer")
        environment.clock.tick(120) #This sets the FPS limit 

    pygame.quit() 

if __name__ == "__main__":
    main()    
