import main
import unittest

class TestProject1(unittest.TestCase):
    # Test crazy_math
    def test_crazy_math(self):
        self.assertEqual(-29, main.crazy_math(4, 3, -2))
        self.assertEqual(6, main.crazy_math(3, 5, 1))
        self.assertEqual(10, main.crazy_math(1, -3, -2))
        self.assertEqual(7, main.crazy_math(5, 2, 3))
        self.assertEqual(9, main.crazy_math(7, -2, 4))
        self.assertEqual(5, main.crazy_math(6, 3, -4))

    # Test str_modify
    def test_str_modify(self):
        self.assertEqual('ngAMAZI', main.str_modify('amazing'))
        self.assertEqual('', main.str_modify(''))
        self.assertEqual('HELLO', main.str_modify('hello'))
        self.assertEqual('APPLE', main.str_modify('APPLE'))
        self.assertEqual(' WorldHELLO', main.str_modify('Hello World'))
        self.assertEqual('a BreadBANAN', main.str_modify('Banana Bread'))

    # Test debugging_1
    def test_debugging_1(self):
        self.assertEqual(32, main.debugging_1())

    # Test debugging_2
    def test_debugging_2(self):
        self.assertEqual(True, main.debugging_2(35))
        self.assertEqual(False, main.debugging_2(6))
        self.assertEqual(True, main.debugging_2(-7))

    # Test num_prop
    def test_num_prop(self):
        self.assertEqual('Positive and Odd', main.num_prop(7))
        self.assertEqual('Positive and Even', main.num_prop(10))
        self.assertEqual('Zero', main.num_prop(0))
        self.assertEqual('Negative and Odd', main.num_prop(-3))
        self.assertEqual('Negative and Even', main.num_prop(-6))

    # Test str_size
    def test_str_size(self):
        self.assertEqual('Very small', main.str_size('abc'))
        self.assertEqual('Small', main.str_size('apple'))
        self.assertEqual('Medium', main.str_size('spanish'))
        self.assertEqual('Large', main.str_size('schedule'))
        self.assertEqual('Very Long', main.str_size('hippopotamus'))
        self.assertEqual('Very small', main.str_size(''))

    # Test complex_condition
    def test_complex_condition(self):
        self.assertEqual(True, main.complex_condition(False, False, True))
        self.assertEqual(True, main.complex_condition(False, False, False))
        self.assertEqual(False, main.complex_condition(True, True, True))
        self.assertEqual(False, main.complex_condition(True, False, True))
        self.assertEqual(False, main.complex_condition(True, True, False))
        self.assertEqual(False, main.complex_condition(True, False, False))
        self.assertEqual(True, main.complex_condition(False, True, True))
        self.assertEqual(False, main.complex_condition(False, True, False))

    # Test has_real_roots
    def test_has_real_roots(self):
        self.assertEqual(True, main.has_real_roots(1,4,4))
        self.assertEqual(True, main.has_real_roots(2,5,3))
        self.assertEqual(False, main.has_real_roots(1,2,2))
        self.assertEqual(True, main.has_real_roots(1,0,0))
        self.assertEqual(True, main.has_real_roots(1,5,6))
        self.assertEqual(False, main.has_real_roots(1,2,4))

    # Test roots
    def test_roots(self):
        self.assertEqual('-2 and 2', main.roots(1,4,4))
        self.assertEqual('No real roots', main.roots(1,2,2))
        self.assertEqual('0', main.roots(1,0,0))
        self.assertEqual('-2 and -3', main.roots(1,5,6))
        self.assertEqual('No real Roots', main.roots(1,2,4))
        self.assertEqual('-5', main.roots(1,10,25))

if __name__ == '__main__':
    unittest.main()
