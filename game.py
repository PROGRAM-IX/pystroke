import pygame
from game_engine import GameEngine
from input_engine import InputEngine
from event_engine import EventEngine

class Game:
    """
    Container and manager for GameEngine instances
    
    @author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, width, height):
        """
        Constructs a new Game, whose screen has the specified width and height

        @type width: int
        @param width: Width of the screen
        
        @type height: int
        @param height: Height of the screen 
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.width = width
        self.height = height
        self.screen = None
        self.engine = None
        self.engines = []
        self.i_e = InputEngine()
        self.e_e = EventEngine(self.i_e)
        
    def start(self):
        """
        Set up the GameEngine and run the game
        
        @author: James Heslin (PROGRAM_IX)
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyStroke")
        self.engines = [GameEngine(self.screen, self.e_e)] # add others here
        self.engine = self.engines[0]
        self.run()
        
    def run(self):
        """
        Runs the GameEngine, switches to another GameEngine, or quits, based on
        returned flags from GameEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        r = self.engine.run()
        while r != 1:
            if r == 0:
                if self.engines.index(self.engine) < len(self.engines) - 1:
                    self.engine = self.engines[self.engines.index(self.engine) + 1]
                    print self.engines.index(self.engine)
                    self.e_e.reset_input()
                else:
                    self.engine = self.engines[0]
            r = self.engine.run()
        pygame.quit()
        raise SystemExit
        
def main():
    """
    Default running parameters for Game
    
    @author: James Heslin (PROGRAM_IX)    
    """
    g = Game(800, 600)
    g.start()
    
if __name__ == "__main__":
    main()
