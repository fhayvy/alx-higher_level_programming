import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertAlmostEqual(max_integer([9, 0, 3]), 9)

        self.assertAlmostEqual(max_integer([0, 40, 50, 30, 20, 10]), 50)

        self.assertAlmostEqual(max_integer([]), None)

        self.assertAlmostEqual(max_integer([2]), 2)

        self.assertAlmostEqual(max_integer([-3, -8, -1, -15]), -1)

        self.assertAlmostEqual(max_integer([-3, -8, 12, -1]), 12)

        self.assertAlmostEqual(max_integer([-9, 12, 4, 19, 20]), 20)
