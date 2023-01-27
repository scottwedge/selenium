#!/usr/bin/env python3

# Imports 
import unittest
import MathFunctions

class KnownValues(unittest.TestCase):
    def test_circleArea_r_10(self):
        result = MathFunctions.circleArea(10)

        # Check correct expected output
        expected = 314
        self.assertEqual(expected, result)

    def test_circleArea_r_1(self):
        result = MathFunctions.circleArea(1)

        # Check correct expected output
        expected = 3.14
        self.assertEqual(expected, result)



if __name__ == "__main__":
    unittest.main()
