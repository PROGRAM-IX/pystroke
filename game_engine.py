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
    def __init__(self, screen, event_e=EventEngine(InputEngine())):
        """
        Constructs a GameEngine
        
        @type screen: pygame.Surface
        @param screen: The screen on which the game will be rendered - this will
        be passed around to other classes
        
        @type event_e: EventEngine
        @param event_e: The EventEngine that this will use to read events
        
        @author: James Heslin (PROGRAM_IX)  
        """
        self.screen = screen
        self.event_e = event_e
        self.draw_e = DrawEngine(screen)
        self.beh_e = BehaviourEngine()
        self.clock = pygame.time.Clock()
        self._hud = HUD()
        
    def update(self):
        """
        Performs per-frame logic
        
        @rtype: int
        @return: Flag to tell Game what to do
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.event_e.update()
        self.clock.tick(60)
        # To switch state
        #if switch_state_condition:
        #    return 0
        
        # To quit 
        #elif quit_condition:
        #    return 1
        
        # To maintain consistency
        #else:
        #    return 2
        
        return 2
    
    def draw(self):
        """
        Draws all necessary elements using the DrawEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.draw_e.begin_draw(pygame.Color(0, 0, 0))
        # Draw your drawables here
        # They must be passed in as lists
        # self.draw_e.draw([some_drawable, some_other_drawable])
        # self.draw_e.draw([another_drawable])
        self.draw_e.end_draw()
        
    def run(self):
        """
        The main loop of the game
        
        @rtype: int
        @return: Flag to tell Game what to do 
        
        @author: James Heslin (PROGRAM_IX)
        """
        while True:
            r = self.update()
            if r == 0 or r == 1:    
                return r
            self.draw()
            