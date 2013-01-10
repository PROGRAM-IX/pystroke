import pygame
from pygame.locals import *

class InputEngine:
    """
    Receives input events from an EventEngine and uses them to maintain an up-
    to-date keyboard/mouse state
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self):
        """
        Constructs a new InputEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.keys = [0] * 1024
        self.mouse_pos = (1,1)
        self.mouse_buttons = [0] * 16
        
    def mouse_motion(self, event):
        """
        Processes MOUSEMOTION events
        
        @type event: pygame.Event
        @param event: A MOUSEMOTION event
        
        @author: James Heslin (PROGRAM_IX)
        """
        if self.mouse_pos is not event.pos:
            self.mouse_pos = event.pos    
    
    def mouse_b_down(self, event):
        """
        Processes MOUSEBUTTONDOWN events
        
        @type event: pygame.Event
        @param event: A MOUSEBUTTONDOWN event
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.mouse_buttons[event.button] = True
    
    def mouse_b_up(self, event):
        """
        Processes MOUSEBUTTONUP events
        
        @type event: pygame.Event
        @param event: A MOUSEBUTTONUP event
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.mouse_buttons[event.button] = False
    
    def key_down(self, event):
        """
        Processes KEYDOWN events
        
        @type event: pygame.Event
        @param event: A KEYDOWN event
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.keys[event.key] = True
        
    def key_up(self, event):
        """
        Processes KEYUP events
        
        @type event: pygame.Event
        @param event: A KEYUP event
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.keys[event.key] = False
        
    def reset(self):
        """
        Reset all the input values
        
        @author: James Heslin (PROGRAM_IX)
        """
        del self.keys
        del self.mouse_pos
        del self.mouse_buttons
        self.keys = [0] * 1024
        self.mouse_pos = (1,1)
        self.mouse_buttons = [0] * 16
        
    def print_all_states(self):
        """
        Print the states of all tracked inputs
        
        @author: James Heslin (PROGRAM_IX)
        """
        print self.keys
        print self.mouse_pos
        print self.mouse_buttons