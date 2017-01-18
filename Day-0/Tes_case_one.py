def Area(b,h):
    return (b*h)/2

import unittest

class Test_A(unittest.TestCase):
    def testArea(self):
        self.assertEqual(Area(3,3), 4.5)
        self.assertEqual(Area(2.8,3.25), 4.55)

if __name__ == '__main__':
    unittest.main()
