# encoding: utf-8
'''Note that for the purposes of this problem, we do not consider changing the orientation of a diagonal edge or adding both diagonal edges to a cell as a different way of making a grid graph rigid.

Let R(m,n) be the number of ways to make the m × n grid graph rigid.
E.g. R(2,3) = 19 and R(5,5) = 23679901

Define S(N) as ∑R(i,j) for 1 ≤ i, j ≤ N.
E.g. S(5) = 25021721.
Find S(100), give your answer modulo 1000000033 '''

import unittest
from main import *

class TestRigidity(unittest.TestCase):
    def test_Foo(self):
        self.assertEqual(True, False)
        
if __name__=='__main__':
    unittest.main()
