import unittest
from bruch.Bruch import *


class TestExtension(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testDoubleDivision(self):
        self.b = self.b / self.b2 / self.b3
        assert (float(self.b) == 0.5)

    def testDoubleMultiplikation(self):
        self.b = self.b * self.b2 * self.b3
        assert (float(self.b) == 4.5)

    def testTupleMult(self):
        z, n = Bruch(3, 4) * Bruch(1, 2)
        assert (Bruch(z, n) == Bruch(3, 8))

    def testTupleDiv(self):
        z, n = Bruch(8, 7) * Bruch(2, 5)
        assert (Bruch(z, n) == Bruch(16, 35))

    def testComplexSub(self):
        z = complex(self.b3) - complex(self.b)
        assert (z == 0.5)
