import math
from math import pi


def volume_cylinder(r, h):
    return int(pi*r**2*h)
    

import unittest

class Test_v(unittest.TestCase):
    def testVolume(self):
        self.assertEqual(volume_cylinder(4,6),301)
        self.assertEqual(volume_cylinder(2,2), 25)


if __name__ == '__main__':
    unittest.main()
