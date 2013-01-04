import pygame
from game_engine import GameEngine

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
        
    def start(self):
        """
        Set up the GameEngine and begin running the game
        
        @author: James Heslin (PROGRAM_IX)
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.engine = GameEngine(self.screen)
        self.engine.run()
        
def main():
    """
    Default running parameters for Game
    
    @author: James Heslin (PROGRAM_IX)    
    """
    g = Game(800, 600)
    g.start()
    
if __name__ == "__main__":
    main()
