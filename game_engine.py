import pygame
from pygame.locals import *
from hud import *

from behaviour_engine import BehaviourEngine
from input_engine import InputEngine
from event_engine import EventEngine
from draw_engine import DrawEngine


class GameEngine:
    def __init__(self, screen):
        i_e = InputEngine()
        self.screen = screen
        self.event_e = EventEngine(i_e)
        self.draw_e = DrawEngine(screen)
        self.beh_e = BehaviourEngine()
        self.clock = pygame.time.Clock()
        self._hud = HUD()
        
    def update(self):
        pass
    
    def draw(self):
        pass
        
    def run(self):
        while True:
            self.update()
            self.draw()
            