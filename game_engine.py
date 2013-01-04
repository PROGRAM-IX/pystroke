import pygame
from pygame.locals import *
from hud import *

from behaviour_engine import BehaviourEngine
from input_engine import InputEngine
from event_engine import EventEngine
from draw_engine import DrawEngine


class GameEngine:
    """
    Generic class to contain all logic for the basic running of the game
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self, screen):
        """
        Constructs a GameEngine
        
        @type screen: pygame.Surface
        @param screen: The screen on which the game will be rendered - this will
        be passed around to other classes
        
        @author: James Heslin (PROGRAM_IX)  
        """
        i_e = InputEngine()
        self.screen = screen
        self.event_e = EventEngine(i_e)
        self.draw_e = DrawEngine(screen)
        self.beh_e = BehaviourEngine()
        self.clock = pygame.time.Clock()
        self._hud = HUD()
        
    def update(self):
        """
        Performs per-frame logic
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.clock.tick(60)
    
    def draw(self):
        """
        Draws all necessary elements using the DrawEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.draw_e.begin_draw(pygame.Color(0, 0, 0))
        pass # Draw your drawables here
        self.draw_e.end_draw()
        
    def run(self):
        """
        The main loop of the game
        
        @author: James Heslin (PROGRAM_IX)
        """
        while True:
            self.update()
            self.draw()
            