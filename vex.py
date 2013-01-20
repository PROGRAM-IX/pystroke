import pygame
from pygame.locals import *
from vector2 import Vector2
from random import *
import math

class Vex():
    """
    Vector sprite class (consider renaming) - consists of a list of points which
    are rendered relative to an x and y at draw time
    
    @author: James Heslin (PROGRAM_IX)    
    """
    radius = 20
    def __str__(self):
        """
        Returns a string containing the x and y of the vector sprite
        
        @rtype: string
        @return: A string containing the x and y of the vector sprite
        
        @author: James Heslin (PROGRAM_IX)
        """
        #string = "Colour: %d, %d, %d" % (self.colour.r, self.colour.g, self.colour.b)
        #string = "Colour:", self.colour.r, self.colour.g, self.colour.b
        string = "Position: %d, %d" % (self.x, self.y)
        #string = string + "Points:"
        #for p in self.points:
            #string = string + p
        return string


    def __init__(self, x, y, colour, points, width, scale_x=1, scale_y=1):
        """
        Constructs a new Vex
        
        @type x: int
        @param x: The X (horizontal) co-ordinate of the vector sprite
        
        @type y: int
        @param y: The Y (vertical) co-ordinate of the vector sprite
        
        @type colour: pygame.Color
        @param colour: The colour of the vector sprite
        
        @type points: list/tuple of tuples (int, int)
        @param points: The points that make up the vector sprite
        
        @type width: int 
        @param width: The width of the vector sprite's lines
        
        @type scale_x: double
        @param scale_x: The horizontal multiplier of the vector sprite's size
        
        @type scale_y: double
        @param scale_y: The vertical multiplier of the vector sprite's size
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.colour = colour
        self.points = points
        self.width = width
        self.x = x
        self.y = y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.rel_dir_vec = Vector2(0, -1) # Points directly up by default
        
        self.lifetime = 1
        
        #self.dir_vec = points[0]
        #print "Direction:", self.dir_vec()
        #print self.__str__()
    
    def dir_vec(self):
        """
        Return a copy of the vector sprite's direction vector (the first vector
        in its list of points), adjusted to have absolute co-ordinates 
        
        @rtype: Vector2
        @return: A copy of the vector sprites's direction vector, with absolute
        co-ordinates
        
        @author: James Heslin (PROGRAM_IX)
        """
        #print self.points[0] + vector2(self.x, self.y)
        
        # Consider: store direction separately, but rotate it when everything
        # else rotates. 
        
        
        v = Vector2(self.points[0].x*self.scale_x, 
                    self.points[0].y*self.scale_y)
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

    def rel_dir(self):
        """
        Returns a copy of the relative direction vector
        
        @rtype: Vector2
        @return: A copy of the relative direction vector
        """
        return Vector2(self.rel_dir_vec.x, self.rel_dir_vec.y)
        

    def draw(self, surface):
        """
        Renders the vector sprite to the surface specified
        
        @type surface: pygame.Surface
        @param surface: The surface onto which the vector sprite is to be 
        rendered
        
        @author: James Heslin (PROGRAM_IX)
        """ 
        
        
        
        pygame.draw.polygon(surface, self.colour, 
                self.get_absolute_points_tuple(), self.width)
        #dir_v = self.dir_vec()
        #pygame.draw.aaline(surface, pygame.Color(255, 0, 0), 
                #(self.x, self.y), (dir_v.x, dir_v.y), 4)

    def update(self, surface): # surface => check collision with outer bounds
        """
        Updates the vector sprite with respect to the specified surface
        
        @type surface: pygame.Surface
        @param surface: The surface to update the vector sprite against
        
        @author: James Heslin (PROGRAM_IX)
        """        
        
        
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

    def distance_to(self, p):
        """
        Returns the distance between the centre of the vector sprite and the 
        specified point
        
        @type p: Vector2
        @param p: The point to compare to the vector sprite
        
        @rtype: double
        @return: The distance between the centre of the vector sprite and the 
        specified point
        
        @author: James Heslin (PROGRAM_IX)
        """
        return (Vector2(self.x, self.y) - p).get_magnitude()
        

    def vector_between(self, p):
        """
        Returns the vector between the vector sprite and the specified point
        
        @type p: Vector2
        @param p: The point to compare to the vector sprite
        
        @rtype: Vector2
        @return: The vector between the vector sprite and the specified point
        
        @author: James Heslin (PROGRAM_IX)
        """
        
        # Remember: Vectors are NOT pass-by-value! 
        # Be more careful in future. 
        
        # What if this took the direction ONLY into account?
        # Normalising won't work - only covers one sector then
       
        # Trying relative vector mathematics
        rel_p = p - Vector2(self.x, self.y)
        # This line is wrong because it means I'm getting the vector between
        # the directional point of this vex, and the point p. Actually I want
        # to get the vector between the centre of the vex and p, so that I can
        # adjust to that vector later.
        #rel_dir = Vector2(self.points[0].x, self.points[0].y)
        
        #direction = self.dir_vec()
        
        #v = rel_dir - rel_p
        return rel_p

    def angle_to_face_point(self, p):
        """
        Return the rotation angle (in radians) required for the vector sprite to 
        face a specified point (face: the vector sprite's direction vector is 
        pointing towards the point)
        
        @type p: Vector2
        @param p: The point to face
        
        @rtype: double
        @return: The rotation angle (in radians) required for the vector sprite
        to face p
        
        @author: James Heslin (PROGRAM_IX)
        """
        p = p - Vector2(self.x, self.y)
        
        angle_p = p.get_angle()
        angle_self = Vector2(self.points[0].x, self.points[0].y).get_angle()
        
        angle = angle_self - angle_p
        
        # I think this should work, theoretically - why doesn't it?
        #angle = self.vector_between(p).get_angle()
        return angle
        
        
    def rotate_to_face_point(self, p):
        """
        Rotate the vex to face a specified point
        
        @type p: Vector2
        @param p: The point to face
        
        @author: James Heslin (PROGRAM_IX)
        """
        angle = self.angle_to_face_point(p)
        
        self.rotate_by_radians(-angle)
        
        
    def rotate_by_radians(self, a):
        """
        Rotate the shape by a given number of radians
        
        @type a: double
        @param a: The number of radians to rotate the vector sprite by
        
        @author: James Heslin (PROGRAM_IX)
        """
        cos_a = math.cos(a) # save these so we only need to do the 
        sin_a = math.sin(a) # call once for each
        for i in self.points:
            old_x = i.x 
            old_y = i.y # preserve old values
            i.x = (old_x*cos_a - old_y*sin_a) # use old values to calculate
            i.y = (old_x*sin_a + old_y*cos_a) # new values
        old_x = self.rel_dir_vec.x
        old_y = self.rel_dir_vec.y
        self.rel_dir_vec.x = (old_x*cos_a - old_y*sin_a)
        self.rel_dir_vec.y = (old_x*sin_a + old_y*cos_a)
        #print "Finished rotating"

    def move_abs(self, x, y, surface): 
        """
        Move the vector sprite in the X/Y plane without leaving the bounds of 
        the specified surface - performs vector calculation to make sure
        diagonal movement is not faster than cardinal
        
        @type x: double
        @param x: The X (horizontal) movement amount
        
        @type y: double
        @param y: The Y (vertical) movement amount
        
        @type surface: pygame.Surface
        @param surface: The surface to use to restrict the movement of the 
        vector sprite
        
        @author: James Heslin (PROGRAM_IX)
        """
        
        #TODO: make a new Vector2 using x and y, then move_rel?
        
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

    def move_rel(self, x, y, surface):
        """
        Move the vector sprite in the X/Y plane without leaving the bounds of 
        the specified surface - assumes all inputs have already been calculated
        to restrict movement speed
        
        @type x: double
        @param x: The X (horizontal) movement amount
        
        @type y: double
        @param y: The Y (vertical) movement amount
        
        @type surface: pygame.Surface
        @param surface: The surface to use to restrict the movement of the 
        vector sprite
        
        @author: James Heslin (PROGRAM_IX)
        """
        if abs(x) > 0 or abs(y) > 0:
            if ((self.x + x < surface.get_width() and self.x + x > 0)
                and (self.y + y < surface.get_height() and self.y + y > 0)):
                #for p in self.points:
                    #p.x += x
                    #p.y += y
                self.x += int(x)
                self.y += int(y)
        

    def get_relative_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to vector sprite 
        position, respective of scale
        
        @rtype: list of tuples (int, int)
        @return: A list of tuples representing the points in the vector sprite,
        with co-ordinates relative to the vector sprite's position, respective 
        of scale
        
        @author: James Heslin (PROGRAM_IX)
        """
        pts = []
        for p in self.points:
            pts.append((p.x*self.scale_x, p.y*self.scale_y))
        return pts
    
    def get_absolute_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to origin, respective 
        of scale
        
        @rtype: list of tuples (int, int)
        @return: A list of tuples representing the points in the vector sprite,
        with co-ordinates relative to the origin, respective of scale
        
        @author: James Heslin (PROGRAM_IX)
        """
        pts = []
        for p in self.points:
            pts.append(((p.x*self.scale_x)+self.x, (p.y*self.scale_y)+self.y))
        return pts

    def get_relative_points_vector2(self):
        """
        Returns a list of Vector2 objects representing 2D points, relative 
        to vector sprite position, respective of scale
        
        @rtype: list of Vector2 objects
        @return: A list of Vector2 objects representing the points in the vector 
        sprite, with co-ordinates relative to the vector sprite's position, 
        respective of scale
        
        @author: James Heslin (PROGRAM_IX)
        """
        pts = []
        for p in self.points:
            pts.append(Vector2(p.x*self.scale_x, p.y*self.scale_y))
        return pts

    def get_absolute_points_vector2(self):
        """
        Returns a list of Vector2 objects representing 2D points, relative 
        to origin, respective of scale
        
        @rtype: list of Vector2 objects
        @return: A list of Vector2 objects representing the points in the vector 
        sprite, with co-ordinates relative to the origin, respective of scale
        
        @author: James Heslin (PROGRAM_IX)
        """
        pts = []
        for p in self.points:
            pts.append(Vector2((p.x*self.scale_x)+self.x, 
                               (p.y*self.scale_y)+self.y))
        return pts
    
    def point_inside(self, v):
        """
        Determines roughly if a given point is inside the vector sprite, can be
        used for crude collision detection
        
        @type v: Vector2
        @param v: The point to check
        
        @rtype: boolean
        @return: True if the point is inside the vector sprite, False otherwise 
        
        @author: James Heslin (PROGRAM_IX)
        """
        max_x = self.points[0].x
        max_y = self.points[0].x
        min_x = max_x
        min_y = max_y
        for i in self.points:
            if i.x*self.scale_x > max_x:
                max_x = i.x*self.scale_x
            elif i.x*self.scale_x < min_x:
                min_x = i.x*self.scale_x
            if i.y*self.scale_y > max_y:
                max_y = i.y*self.scale_y
            elif i.y*self.scale_y < min_y:
                min_y = i.y*self.scale_y
        max_x = max_x + self.x
        max_y = max_y + self.y
        min_x = min_x + self.x
        min_y = min_y + self.y
        
        if v.x < max_x and v.y < max_y and v.x > min_x and v.y > min_y:
            return True
        else:
            return False
    
