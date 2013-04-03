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
        