import pygame
from values import*

class buttons():
    # initializes values when an instance of the class is created
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color                              # sets the color to color
        self.x = x                                      # sets the x position to x
        self.y = y                                      # sets the y position to y
        self.width = width                              # sets the width of the button to width
        self.height = height                            # sets the height of the button to height
        self.text = text                                # sets the text for the button (if any) to text

    # draws the buttons
    def draw_button(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0) # draws a rectangle on the screen, with a black outline
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0) # draws the button rectangle
        
        if self.text != '':                             # if there is text
            font = pygame.font.SysFont('corbel', 25)    # set the font to corbel, size 25
            text = font.render(self.text, 1, (255,255,255)) # render the text
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2))) # place the text onto the button

    # checks if the mouse is in the same position as the button
    def is_hovering(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width: # if the mouse x position is greater than the button x position and the mouse x position is less than the button x position and the button width
            if pos[1] > self.y and pos[1] < self.y + self.height: # check if the mouse y position is greater than the button y positon and the mouse y position is less than the button y position and the button height
                return True                             # return True
            
        return False                                    # otherwise return False