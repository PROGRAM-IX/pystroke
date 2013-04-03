import unittest
import math
from pystroke.vector2 import Vector2


class TestVector2(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_str(self):
        self.assertEqual(self.v1.__str__(), "(4, -3)")
        self.assertEqual(self.v2.__str__(), "(100, -150)")
        
class TestMagnitude(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_magnitude(self):
        self.assertEqual(self.v1.get_magnitude(), 5)
        self.assertEqual(self.v2.get_magnitude(), math.sqrt(100**2 + (-150)**2))

        
class TestNormalised(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_normalised(self):
        self.assertEqual(self.v1.normalised().get_magnitude(), 1)
        self.assertEqual(self.v2.normalised().get_magnitude(), 1)

class TestDotProduct(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_dot_product(self):
        self.assertEqual(self.v1.dot_product(self.v2), 850)
        
class TestCrossProduct(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_cross_product(self):
        self.assertEqual(self.v1.cross_product(self.v2), -300)
        
class TestGetAngle(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_get_angle(self):
        self.assertEqual(self.v1.get_angle(), math.atan2(-3, 4))
        
class TestAdd(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_add(self):
        self.assertEqual((self.v1 + self.v2).x, 104)
        self.assertEqual((self.v1 + self.v2).y, -153)
        
class TestSubtract(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_subtract(self):
        self.assertEqual((self.v1 - self.v2).x, -96)
        self.assertEqual((self.v1 - self.v2).y, 147)
        
class TestNeg(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_neg(self):
        self.assertEqual((-self.v1).x, -4)
        self.assertEqual((-self.v1).y, 3)
        
class TestMul(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_mul(self):
        self.assertEqual((self.v1*10).x, 40)
        self.assertEqual((self.v1*10).y, -30)
        
class TestDiv(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2(4, -3)
        self.v2 = Vector2(100, -150)
        
    def test_div(self):
        self.assertEqual((self.v1/10.0).x, .40)
        self.assertEqual((self.v1/10.0).y, -.30)