def fact(n):
 
    if n == 0:
        return 1
    return n * fact(n -1)

def div(n):
    
    res = 10 / n
    return res


def main(n):
    res = fact(n)
    print(res)



import unittest

import math
from math import factorial
from math import factorial as fact


class TestFactorial(unittest.TestCase):


    def test_fact(self):
        res = fact(12)
        self.assertEqual(res, 479001600)

    def test_error(self):
        
        self.assertRaises(ZeroDivisionError, div, 0)



if __name__ == '__main__':
    unittest.main()
