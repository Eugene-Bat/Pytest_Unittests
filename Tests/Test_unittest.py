from unittest import TestCase, main
from Pytest_Unittests.main import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('6-4'), 2)

    def test_multiply(self):
        self.assertEqual(calculator('5*3'), 15)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2)

    def test_no_sigbs(self):
        with self.assertRaises(ValueError) as e:
            calculator('qwerty')
        self.assertEqual('Must contain at least one of the allowed signs', e.exception.args[0])

    def test_two_sigbs(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+3+7')
        self.assertEqual('The expression must contain two integers and one sign', e.exception.args[0])

    def test_many_sigbs(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+3+7*2/3')
        self.assertEqual('The expression must contain two integers and one sign', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+3+7')
        self.assertEqual('The expression must contain two integers and one sign', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+f')
        self.assertEqual('The expression must contain two integers and one sign', e.exception.args[0])


if __name__ == '__main__':
    main()


