import unittest
from scripts import *


class TestFunctions(unittest.TestCase):


    def testtwomaxsum(self):

        self.assertEqual(two_max_sum(17, 10, 13), 30)

    def testtwomaxsum2(self):

        self.assertNotEqual(two_max_sum(11, 7, 10), 19)

    def testintfunc(self):

        self.assertEqual(int_func('it is working'), 'It Is Working')

    def testmyfunc(self):

        self.assertEqual(my_func([2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]),
                         [23, 1, 3, 10, 4, 11])

    def testexcemption(self):

        self.failureException(division_1(2, 0), 'Cannot divide by zero')

    def testraises(self):

        self.assertRaises(DivisionByZero, division_2, 4, 0)

    def testmyfunccount1(self):

        self.assertIn(4, my_func_count(2, 7))

    def testmyfunccount2(self):

        self.assertNotIn(8, my_func_count(2, 7))

    def testclassobjects1(self):

        self.assertIsNot(Cell(2), Cell(2))

    def testclassobjects2(self):

        self.assertGreaterEqual(Cell(2).quantity, Cell(2).quantity)

    def testclassobjects3(self):

        self.assertIsInstance(Cell(9), Cell)


if __name__ == '__main__':
    unittest.main()