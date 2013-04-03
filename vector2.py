import math

class Vector2():
    """
    A two-dimensional vector
    
    @author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, x=0.0, y=0.0):
        """
        Constructs a new Vector2
        
        @type x: double
        @param x: X (horizontal) co-ordinate of vector
        
        @type y: double
        @param y: Y (vertical) co-ordinate of vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.x = x
        self.y = y
    
    def __str__(self):
        """
        Returns a string with the vector's co-ordinates
        
        @rtype: string
        @return: A string containing the vector's co-ordinates
        
        @author: James Heslin (PROGRAM_IX)
        """
        return "(%s, %s)" % (self.x, self.y)
    
    @staticmethod
    def from_points(a, b):
        """
        Returns a new Vector2 with the co-ordinates of the difference between
        the two points
        
        @type a: tuple/list of two ints
        @param a: The first point to use in constructing the new Vector2
        
        @type b: tuple/list of two ints
        @param b: The second point to use in constructing the new Vector2
        
        @rtype: Vector2
        @return: A new Vector2 constructed from the inputted points
    
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(b[0]-a[0], b[1]-a[1])

    def get_magnitude(self):
        """
        Returns the magnitude of the vector
        
        @rtype: double
        @return: The magnitude of the vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        
        return math.sqrt(self.x**2 + self.y**2)

    def normalised(self):
        """
        Returns a normalised copy of the vector
        
        @rtype: Vector2
        @return: Normalised copy of the vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        magnitude = self.get_magnitude()
        if not magnitude == 0:
            return Vector2(self.x * 1/magnitude, self.y * 1/magnitude)
        else:
            return Vector2(self.x, self.y)
    
    def dot_product(self, other):
        """
        Returns the dot product of the vector and the input vector
        
        @type other: Vector2
        @param other: The vector to dot product against
        
        @rtype: double
        @return: The dot product of the vector and the input vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        # A dot B = A B cos theta = |A||B| cos theta
        # or A dot B = AxBx + AyBy + AzBz
        return self.x*other.x + self.y*other.y
    
    def cross_product(self, other):
        """
        Returns the cross product of the vector and the input vector
        
        @type other: Vector2
        @param other: The vector to cross product against
        
        @rtype: double
        @return: The cross product of the vector and the input vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        return self.x * other.y - self.y * other.x 
    
    @staticmethod
    def clamp(x, a, b):
        """
        'Clamp' the value of x between a and b, i.e., return x if it is between
        a and b, a if x is lower than a, and b if x is larger than b
        
        @type x: double
        @param x: The number to clamp
        
        @type a: double
        @param a: The lower bound of x's clamp
        
        @type b: double
        @param b: The upper bound of x's clamp
        
        @rtype: double
        @return: The clamped value of x
        
        @author: James Heslin (PROGRAM_IX)
        """
        return min(max(x, a), b)

    def get_angle(self):
        """
        Returns the angle this vector is pointing to 
        
        @rtype: double
        @return: The angle this vector points to (in radians)        
        
        @author: James Heslin (PROGRAM_IX)
        """
        return math.atan2(self.y, self.x)
    
    def __add__(self, other):
        """
        Add the vector to other and return the result
        
        @type other: Vector2
        @param other: The vector to add
        
        @rtype: Vector2
        @return: The result of the vector being added to other
        
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtract other from the vector and return the result
        
        @type other: Vector2
        @param other: The vector to subtract
        
        @rtype: Vector2
        @return: The result of other being subtracted from the vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """
        Negate the vector and return the result
        
        @rtype: Vector2
        @return: The negated vector
        
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(-self.x, -self.y)

    def __mul__(self, sca):
        """
        Multiply the vector by other and return the result
        
        @type sca: double
        @param sca: The scalar to multiply by
        
        @rtype: Vector2
        @return: The result of the vector being multiplied by sca
        
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(self.x * sca, self.y * sca)

    def __div__(self, sca):
        """
        Divide the vector by sca and return the result
        
        @type sca: double
        @param sca: The scalar to divide by
        
        @rtype: Vector2
        @return: The result of the vector being divided by sca
        
        @author: James Heslin (PROGRAM_IX)
        """
        return Vector2(self.x / sca, self.y / sca)


