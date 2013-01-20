import pygame
from pygame.locals import *
import copy

class HUDElement:
    """
    Generic part of a heads-up display
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self, label, colour, visible=True):
        """
        Constructs a new HUDElement
        
        @type label: string
        @param label: Identifier of the element
        
        @type colour: pygame.Colour
        @param colour: Colour of the element
        
        @type visible: boolean
        @param visible: Whether the element is visible
        
        @author: James Heslin (PROGRAM_IX) 
        """
        self.label = label
        self.colour = colour
        self.visible = visible
        
    def draw(self, screen):
        """
        Draw the element to the screen
        
        @type screen: pygame.Surface
        @param screen: The surface onto which the game will be rendered
        
        @author: James Heslin (PROGRAM_IX)
        """
        pass

class HUDText(HUDElement):
    """
    An element of a heads-up display consisting of text
    
    @author: James Heslin (PROGRAM_IX)
    """    
    letters = { 
        'a': ((-5, -10), (-5, 15), (-5, 0), (5, 0), (5, 15), 
              (5, -10), (-5, -10)),
        'b': ((-5, -10), (-5, 15), (5, 15), (5, 0), (-5, 0),
              (0, 0), (0, -10), (-5, -10)),
        'c': ((5, -10), (-5, -10), (-5, 15), (5, 15)),
        'd': ((0, -10), (-5, -10), (-5, 15), (0, 15), (5, 10), 
              (5, -5), (0, -10)),
        'e': ((5, -10), (-5, -10), (-5, 0), (0, 0), (-5, 0),
              (-5, 15), (5, 15)),
        'f': ((5, -10), (-5, -10), (-5, 0), (0, 0), (-5, 0),
              (-5, 15)),
        'g': ((5, -10), (-5, -10), (-5, 15), (5, 15), (5, 0), 
              (0, 0)),
        'h': ((-5, -10), (-5, 15), (-5, 0), (5, 0), (5, -10), 
              (5, 15)),
        'i': ((-5, -10), (5, -10), (0, -10), (0, 15), (-5, 15), 
              (5, 15)),
        'j': ((-5, -10), (5, -10), (0, -10), (0, 15), (-5, 15), 
              (-5, 10)),
        'k': ((-5, -10), (-5, 0), (5, -10), (-5, 0), (5, 15), 
              (-5, 0), (-5, 15)),
        'l': ((-5, -10), (-5, 15), (5, 15)),
        'm': ((-5, 15), (-5, -10), (0, -10), (0, 0), (0, -10), 
              (5, -10), (5, 15)),
        'n': ((-5, 15), (-5, -10), (5, 15), (5, -10)),
        'o': ((-5, -10), (-5, 15), (5, 15), (5, -10), (-5, -10)),
        'p': ((-5, 15), (-5, -10), (5, -10), (5, 0), (-5, 0)),
        'q': ((-5, -10), (-5, 10), (0, 10), (0, 15), (5, 15),
              (0, 15), (0, 10), (5, 10), (5, -10), (-5, -10)),
        'r': ((-5, 15), (-5, -10), (5, -10), (5, 0), (-5, 0),
              (5, 15)),
        's': ((5, -10), (-5, -10), (-5, 0), (5, 0), (5, 15), 
              (-5, 15)),
        't': ((-5, -10), (5, -10), (0, -10), (0, 15)),
        'u': ((-5, -10), (-5, 15), (5, 15), (5, -10)),
        'v': ((-5, -10), (0, 15), (5, -10)),
        'w': ((-5, -10), (-5, 15), (0, 15), (0, 0), (0, 15), 
              (5, 15), (5, -10)),
        'x': ((-5, -10), (5, 15), (0, 0), (-5, 15), (5, -10)),
        'y': ((-5, -10), (0, 0), (-5, 15), (5, -10)),
        'z': ((-5, -10), (5, -10), (-5, 15), (5, 15)),
        '1': ((-5, -5), (0, -10), (0, 15), (-5, 15), (5, 15)),
        '2': ((-5, -5), (-5, -10), (5, -10), (5, -5), (-5, 15), (5, 15)),
        '3': ((-5, -10), (5, -10), (0, 0), (5, 5), (0, 15), (-5, 15)),
        '4': ((0, 15), (0, -10), (-5, 0), (5, 0)),
        '5': ((5, -10), (-5, -10), (-5, 0), (0, 0), (5, 5), (5, 10),
              (0, 15), (-5, 15)),
        '6': ((5, -10), (-5, 0), (-5, 15), (5, 15), (5, 0), (-5, 0)),
        '7': ((-5, -10), (5, -10), (-5, 15)),
        '8': ((-5, -10), (5, -10), (5, -5), (0, 0), (-5, 5), 
              (-5, 15), (5, 15), (5, 5), (0, 0), (-5, -5), (-5, -10)),
        '9': ((5, 15), (5, -10), (-5, -10), (-5, 0), (5, 0)),
        '0': ((5, 15), (-5, -10), (-5, 15), (5, 15), (5, -10), (-5, -10))
       
       }
    def __init__(self, label, colour, text, pos, size, width, visible=True):
        """
        @type label: string
        @param label: Identifier of the text
        
        @type colour: pygame.Color
        @param colour: Colour of the text
        
        @type text: string
        @param text: Text to display 
        
        @type pos: list/tuple containing two ints
        @param pos: Coordinates of text start point
        
        @type visible: boolean
        @param visible: Whether the text is visible
        
        @author: James Heslin (PROGRAM_IX)
        """
        HUDElement.__init__(self, label, colour, visible)
        self.text = text
        self.pos = pos
        self.size = size
        self.width = width
        
    def draw(self, screen):
        """
        Render the text to the screen
        
        @type screen: pygame.Surface
        @param screen: The screen onto which the text should be rendered
        
        @author: James Heslin (PROGRAM_IX)
        """
        c_pos = self.pos
        for letter in xrange(len(self.text)):
            if self.text[letter] in self.letters:
                a = self.letters[self.text[letter]]
                last = a[0]
                for pt in a:
                    pygame.draw.line(screen, self.colour, 
                                     (last[0]*self.size+c_pos[0], 
                                        last[1]*self.size+c_pos[1]), 
                                     (pt[0]*self.size+c_pos[0],
                                        pt[1]*self.size+c_pos[1]),
                                     self.width)
                    last = pt
                #print "DRAWING",self.text[letter]
            c_pos = (c_pos[0] + self.size * 15, c_pos[1])


class HUDLine(HUDElement):
    """
    An element of a heads-up display consisting of a line
    
    @author: James Heslin (PROGRAM_IX)
    """    
    def __init__(self, label, colour, line, visible=True):
        """
        Constructs a new HUDLine
        
        @type label: string
        @param label: Identifier of the line
        
        @type colour: pygame.Color
        @param colour: Colour of the line 
        
        @type line: list/tuple containing start position tuple (int, int),
        end position tuple (int, int), and width (int)
        @param line: Line arguments
        
        @type visible: boolean
        @param visible: Whether the line is visible
        
        @author: James Heslin (PROGRAM_IX)
        """
        HUDElement.__init__(self, label, colour, visible)
        self.line = line
    
    def draw(self, screen):
        """
        Render the line to the screen
        
        @type screen: pygame.Surface
        @param screen: The screen onto which the line should be rendered
        
        @author: James Heslin (PROGRAM_IX)
        """
        pygame.draw.line(screen, self.colour, self.line[0], self.line[1], 
                         self.line[-1])
        
class HUDPolygon(HUDElement):
    """
    An element of a heads-up display consisting of a polygon
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self, label, colour, lines, visible=True):
        """
        
        @type label: string
        @param label: Identifier of the polygon
        
        @type colour: pygame.Colour
        @param colour: Colour of the polygon 
        
        @type lines: list/tuple containing a tuple of points (each (int, int)) 
        and an int 
        @param lines: Lines portion of the element

        @type visible: boolean
        @param visible: Whether the element is visible

        @author: James Heslin (PROGRAM_IX)
        """
        HUDElement.__init__(self, label, colour, visible)
        self.lines = lines
        
    def draw(self, screen):
        """
        Render the polygon to the screen
        
        @type screen: pygame.Surface
        @param screen: The screen onto which the polygon is to be rendered
        
        @author: James Heslin (PROGRAM_IX)
        """
        pygame.draw.polygon(screen, self.colour, self.lines[:-1], 
                            self.lines[-1])
    
class HUD:
    """
    A heads-up display, which comprises various visual elements displayed on a
    screen to give information to a player
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self):
        """
        Constructs a new HUD
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.elements = []
    
    def add(self, hud_el):
        """
        Add a new element to the HUD
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.elements.append(hud_el)
        
    def remove(self, hud_el):
        """
        Remove an element from the HUD
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.elements.remove(hud_el)
        
    def draw(self, screen):
        """
        Renders all elements of the HUD to the screen
        
        @type screen: pygame.Surface
        @param screen: The screen onto which the HUD is to be rendered
        
        @author: James Heslin (PROGRAM_IX)
        """
        for e in self.elements:
            if e.visible:
                e.draw(screen)
            
    def get(self, label):
        """
        Returns a HUDElement with matching label from elements, otherwise
        returns None
        
        @type label: string
        @param label: The label of the HUDElement to retrieve
        
        @rtype: HUDElement or None
        @return: The HUDElement with the specified label
        
        @author: James Heslin (PROGRAM_IX)
        """
        for e in self.elements:
            if e.label == label:
                return e
        return None
