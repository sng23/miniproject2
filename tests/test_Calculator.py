import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result(self):        
        self.assertEqual(self.calculator.result, 0)

    def test_add(self):
        result = 8
        self.assertEqual(self.calculator.add(3, 5), result)
        self.assertEqual(self.calculator.result, result)

    def test_subtract(self):
        result = -2
        self.assertEqual(self.calculator.subtract(3, 5), result)
        self.assertEqual(self.calculator.result, result)

    def test_multiply(self):
        result = 15
        self.assertEqual(self.calculator.multiply(3, 5), result)
        self.assertEqual(self.calculator.result, result)

    def test_divide(self):
        result = 3
        self.assertEqual(self.calculator.divide(15, 5), result)
        self.assertEqual(self.calculator.result, result)

    def test_square(self):
        result = 9
        self.assertEqual(self.calculator.square(3), result)
        self.assertEqual(self.calculator.result, result)

    def test_squareroot(self):
        result = 3
        self.assertEqual(self.calculator.squareroot(9), result)
        self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
