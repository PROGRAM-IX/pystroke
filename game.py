import pygame
from game_engine import GameEngine

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.engine = None
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.engine = GameEngine(self.screen)
        self.engine.run()
        
def main():
    g = Game(800, 600)
    g.start()
    
if __name__ == "__main__":
    main()
