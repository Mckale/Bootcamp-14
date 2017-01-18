
def Area_triangle(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    


import unittest

class Test_even_odd(unittest.TestCase):
    def even_odd(self):
        self.assertEqual(volume_cylinder(-12),even)
        self.assertEqual(volume_cylinder(0), even)
        self.assertEqual(volume_cylinder(7), odd)

if __name__ == '__main__':
    unittest.main()
