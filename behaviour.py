from vector2 import Vector2
import math
from random import randint

class Behaviour:
    """
    Stores a modular behaviour that can be added to a game entity
    
    @author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, name):
        """
        Creates a new Behaviour
        
        @type name: string
        @param name: The name of the Behaviour
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.name = name
    
    def process(self, entity):
        """
        Performs the operations making up the Behaviour on the game entity
        
        @type entity: Vex
        @param entity: The game entity affected by the Behaviour
        
        @author: James Heslin (PROGRAM_IX)
        """
        print "Processing %s Behaviour" % (self.name)