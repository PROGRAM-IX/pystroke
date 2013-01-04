import pygame
from pygame.locals import *

class EventEngine:
    """
    Reads the event queue and passes events to other engines
    
    @author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, i_e):
        """
        Takes an InputEngine and passes all relevant events to it
        
        @type i_e: InputEngine
        @param i_e: InputEngine to which input events should be passed
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.input = i_e
    
    def update(self):
        """
        Pulls all relevant events from the event queue and passes
        them to the appropriate engines
        
        @author: James Heslin (PROGRAM_IX)
        """
        for e in pygame.event.get():
            if e.type == MOUSEMOTION:
                self.input.mouse_motion(e)
            elif e.type == MOUSEBUTTONDOWN:
                self.input.mouse_b_down(e)
            elif e.type == MOUSEBUTTONUP:
                self.input.mouse_b_up(e)
            elif e.type == KEYDOWN:
                self.input.key_down(e)
            elif e.type == KEYUP:
                self.input.key_up(e)
    
    def print_input_states(self):
        """
        Prints the states of the InputEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.input.print_all_states()