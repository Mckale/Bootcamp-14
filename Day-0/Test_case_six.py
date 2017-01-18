import math

def quadratic_equation(a, b, c):
 
    d = b ** 2 - 4 * a * c
 
    if d >= 0:
 
        disc = math.sqrt(d)
 
        root1 = (-b + disc) / (2 * a)
 
        root2 = (-b - disc) / (2 * a)
 
        return(root1, root2)
 
import unittest

class Test_even_odd(unittest.TestCase):
    def even_odd(self):
        self.assertEqual(quadratic_equation(2,1,0),1)
        
if __name__ == '__main__':
    unittest.main()
 
