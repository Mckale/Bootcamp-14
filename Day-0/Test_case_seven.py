def Area_triangle(b,h):
    return 1/2*b*h

print(Area_triangle(4,4))


import unittest

class Test_even_odd(unittest.TestCase):
    def even_odd(self):
        self.assertEqual(Area_triangle(4,4),8.0)

if __name__ == '__main__':
    unittest.main()
