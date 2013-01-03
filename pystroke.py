import math
from random import randint
import pygame
from pygame.locals import *
import copy


class BehaviourEngine:
    def __init__(self, beh_dict={}):
        self.beh_dict = beh_dict
        
    def update(self):
        pass

class Behaviour:
    
    def __init__(self, name):
        self.name = name
    
    def process(self):
        pass

class DrawEngine:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, drawables):
        """Presumes everything in the drawables list has a draw()
        method, and draws all of them to screen."""
        for d in drawables:
            d.draw(self.screen)
            
    def begin_draw(self, colour):
        self.screen.fill(colour)
        
    def end_draw(self):
        pygame.display.update()
        
class EventEngine:
    """Manages the event queue and passes events to other engines"""
    
    def __init__(self, i_e):
        """Takes an input_engine and passes all relevant events to it"""
        self.input = i_e
    
    def update(self):
        """Pulls all relevant events from the event queue and passes
        them to the appropriate engines"""
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
    
    def get_input(self):
        self.input.get_all()

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

class HUDElement:
    def __init__(self, label, colour):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        """
        self.label = label
        self.colour = colour
        
    def draw(self, screen):
        """Draw the element to the screen"""
        pass

class HUDText(HUDElement):
    
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
    def __init__(self, label, colour, text, pos, size, width):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        text: text portion ofthe element 
        pos: coordinates of element
        """
        
        HUDElement.__init__(self, label, colour)
        self.text = text
        self.pos = pos
        self.size = size
        self.width = width
        
    def draw(self, screen):
        """Render the text to the screen"""
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
    def __init__(self, label, colour, line):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        line: line portion of the element
            (start pos tuple, end pos tuple, width)
        """
        HUDElement.__init__(self, label, colour)
        self.line = line
    
    def draw(self, screen):
        """Render the line to the screen"""
        pygame.draw.line(screen, self.colour, self.line[0], self.line[1], 
                         self.line[-1])
        
class HUDPolygon(HUDElement):
    def __init__(self, label, colour, lines):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        lines: lines portion of the element
            (points tuple, width)
        """
        HUDElement.__init__(self, label, colour)
        self.lines = lines
        
    def draw(self, screen):
        """Render the polygon to the screen"""
        pygame.draw.polygon(screen, self.colour, self.lines[:-1], 
                            self.lines[-1])
    
class HUD:
    def __init__(self):
        self.elements = []
    
    def add(self, hud_el):
        self.elements.append(hud_el)
        
    def draw(self, screen):
        """Draws all elements of the HUD to the screen"""
        for e in self.elements:
            e.draw(screen)
            
    def get(self, id):
        """Returns a hud_element with matching id from elements, otherwise
        returns None"""
        for e in self.elements:
            if e.label == id:
                return e
        return None

class InputEngine:
    def __init__(self):
        self.keys = [0] * 1024
        self.mouse_pos = (1,1)
        self.mouse_buttons = [0] * 16
        
    def mouse_motion(self, event):
        if self.mouse_pos is not event.pos:
            self.mouse_pos = event.pos    
    
    def mouse_b_down(self, event):
        self.mouse_buttons[event.button] = True
    
    def mouse_b_up(self, event):
        self.mouse_buttons[event.button] = False
    
    def key_down(self, event):
        self.keys[event.key] = True
        
    def key_up(self, event):
        self.keys[event.key] = False
        
    def get_all(self):
        print self.keys
        print self.mouse_pos
        print self.mouse_buttons

class Vector2():
 
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalised(self):
        magnitude = self.get_magnitude()
        if not magnitude == 0:
            return Vector2(self.x * 1/magnitude, self.y * 1/magnitude)
        else:
            return Vector2(self.x, self.y)
    
    # my dot product function
    def dot_product(self, other):
        # A dot B = A B cos theta = |A||B| cos theta
        # or A dot B = AxBx + AyBy + AzBz
        return self.x*other.x + self.y*other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x 
    
    @staticmethod
    def clamp(x, a, b):
        return min(max(x, a), b)

    def radians_between(self, other):
        own = Vector2(self.x, self.y)
        v = Vector2(other.x, other.y)
        own.normalise()
        v.normalise()
        d_p = (self.dot_product(other))
        mag_self = own.get_magnitude()
        mag_other = v.get_magnitude()
        cos_of_angle = d_p/(mag_self*mag_other)
        return math.acos(cos_of_angle)

    
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self, rhs):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

class Vex():
    radius = 20
    def __str__(self):
        #string = "Colour: %d, %d, %d" % (self.colour.r, self.colour.g, self.colour.b)
        #string = "Colour:", self.colour.r, self.colour.g, self.colour.b
        string = "Position: %d, %d" % (self.x, self.y)
        #string = string + "Points:"
        #for p in self.points:
            #string = string + p
        return string


    def __init__(self, x, y, colour, points, width):
        self.colour = colour
        self.points = points
        self.width = width
        self.x = x
        self.y = y
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        #self.dir_vec = points[0]
        #print "Direction:", self.dir_vec()
        #print self.__str__()
    
    def dir_vec(self):
        #print self.points[0] + vector2(self.x, self.y)
        
        # Consider: store direction separately, but rotate it when everything
        # else rotates. 
        
        
        v = Vector2(self.points[0].x, self.points[0].y)
        """
        # Trying to avoid weird edge cases where the mouse is close to the 
        # rotating body
        if v.x < self.radius or v.y < self.radius:
            v = v * self.radius
        
        # Trying to normalise v without losing directionality
        if v.x > v.y and abs(v.x) > 0 and abs(v.y) > 0:
            v = v/(v.x)
        elif v.y > v.x and abs(v.x) > 0 and abs(v.y) > 0:
            v = v/(v.y)
        """
        return v + Vector2(self.x, self.y)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.colour, 
                self.get_absolute_points_tuple(), self.width)
        #dir_v = self.dir_vec()
        #pygame.draw.aaline(surface, pygame.Color(255, 0, 0), 
                #(self.x, self.y), (dir_v.x, dir_v.y), 4)

    def update(self, surface): # surface => check collision with outer bounds
        
        """
        if ((self.x < surface.get_width() and self.x > 0)
            and (self.y < surface.get_height() and self.y > 0)):
        if self.xMod % 5 == 0:
            self.xMod = -self.xMod - 1
        else:
            self.xMod -= 2
        if self.yMod % 5 == 0:
            self.yMod = -self.yMod - 1
        else:
            self.yMod -= 2
        for p in self.points:
            p.x += self.xMod
            p.y += self.yMod
        self.x += self.xMod
        self.y += self.yMod
        """
        #for p in self.points:
            #p.x += self.xMod
            #p.y += self.yMod
        #self.x += self.xMod
        #self.y += self.yMod
        #print"DERP"
        if self.move_up:
            self.move(0, -10, surface)
        elif self.move_down:
            self.move(0, 10, surface)
        elif self.move_left:
            self.move(-10, 0, surface)
        elif self.move_right:
            self.move(10, 0, surface)

    #def is_facing_point(self, x, y):

    def vector_between(self, p):
        # What if this took the direction ONLY into account?
        # Normalising won't work - only covers one sector then
       
        # Trying relative vector mathematics
        p = p - Vector2(self.x, self.y)
        direction = Vector2(self.points[0].x, self.points[0].y)
        #direction = self.dir_vec()
        v = p - direction
        return v

    def angle_to_face_point(self, p):
        v = self.vector_between(p)
        #if v.normalised() is not vector2(0,0):
        # Getting consistency by forcing angle to points on the 360deg circle
        #angle_deg = int(math.atan2(v.x, v.y) * (180 / math.pi))
        #angle = angle_deg / (180 / math.pi)
        # This is wrong, should be y, x
        angle = math.atan2(v.x, v.y)
        #print angle_deg, angle
        #angle_deg = int(angle * 180/math.pi)
        #angle = float(angle_deg) / 180/math.pi
        #print angle_deg
        #if int(angle) == 0:
        return angle
        #else:
            #return 0
        
    def rotate_to_face_point(self, p):
        """Rotate the vex to face a point x, y"""
        # Rotation doesn't work continuously unless the start point is always
        # the same. This sets it.
        angle_start = self.angle_to_face_point(Vector2(self.x, self.y))
        self.rotate_by_radians(angle_start)
        # For some reason everything points the wrong way. Simply reverse the
        # angle here.
        self.rotate_by_radians(math.pi)
        angle = self.angle_to_face_point(p)
        angle_deg = int(angle * (180/math.pi))
        #print angle, angle * 180/math.pi
        #if angle_deg is not 0:
        self.rotate_by_radians(-angle)
        pass    
        #print angle_deg, angle, self.points[0]
        #print self.dir_vec().normalised()
        
    def rotate_by_radians(self, a):
        """Rotate the shape by a given number of radians"""
        cos_a = math.cos(a) # save these so we only need to do the 
        sin_a = math.sin(a) # call once for each
        for i in self.points:
            old_x = i.x 
            old_y = i.y # preserve old values
            i.x = (old_x*cos_a - old_y*sin_a) # use old values to calculate
            i.y = (old_x*sin_a + old_y*cos_a) # new values
        #print "Finished rotating"

    def move(self, x, y, surface): 
        if abs(x) > 0 or abs(y) > 0:
            if abs(x) > 0 and abs(y) > 0:
                x = x * .707
                y = y * .707
            if ((self.x + x < surface.get_width() and self.x + x > 0)
                and (self.y + y < surface.get_height() and self.y + y > 0)):
                #for p in self.points:
                    #p.x += x
                    #p.y += y
                self.x += int(x)
                self.y += int(y)

    def get_relative_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to vex position.
        """
        pts = []
        for p in self.points:
            pts.append((p.x, p.y))
        return pts
    
    def get_absolute_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to origin.
        """
        pts = []
        for p in self.points:
            pts.append((p.x+self.x, p.y+self.y))
        return pts

    def get_relative_points_vector2(self):
        """
        Returns a list of vector2 objects representing 2D points, relative 
        to vex position.
        """
        pts = []
        for p in self.points:
            pts.append(Vector2(p.x, p.y))
        return pts

    def get_absolute_points_vector2(self):
        """
        Returns a list of vector2 objects representing 2D points, relative 
        to origin.
        """
        pts = []
        for p in self.points:
            pts.append(Vector2(p.x+self.x, p.y+self.y))
        return pts
    
    def point_inside(self, v):
        """Determines roughly if a given point is inside the vex"""
        max_x = self.points[0].x
        max_y = self.points[0].x
        min_x = max_x
        min_y = max_y
        for i in self.points:
            if i.x > max_x:
                max_x = i.x
            elif i.x < min_x:
                min_x = i.x
            if i.y > max_y:
                max_y = i.y
            elif i.y < min_y:
                min_y = i.y
        max_x = max_x + self.x
        max_y = max_y + self.y
        min_x = min_x + self.x
        min_y = min_y + self.y
        
        if v.x < max_x and v.y < max_y and v.x > min_x and v.y > min_y:
            return True
        else:
            return False
    
