import pygame
from pygame.locals import *

class DrawEngine:
    """
    Abstracts the calls to Vex.draw() and other drawing methods
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, drawables):
        """
        Presumes everything in the drawables list has a draw()
        method, and draws all of them to screen.
        
        @type drawables: list
        @param drawables: The list of objects to draw (all must have a draw()
        method)
        
        @author: James Heslin (PROGRAM_IX)
        """
        for d in drawables:
            d.draw(self.screen)
            
    def begin_draw(self, colour):
        """
        Clears the screen to prepare for drawing
        
        @type colour: pygame.Color
        @param colour: The colour to fill the screen with
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.screen.fill(colour)
        
    def end_draw(self):
        """
        Updates the screen after draws have finished
        
        @author: James Heslin (PROGRAM_IX)
        """
        pygame.display.update()