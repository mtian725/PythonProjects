import main
import unittest

class TestProject3(unittest.TestCase):
    def test_basic_recurrence(self):
        self.assertEqual(2, main.basic_recurrence(0))
        self.assertEqual(11, main.basic_recurrence(1))
        self.assertEqual(119, main.basic_recurrence(3))
        self.assertEqual(1091, main.basic_recurrence(5))

    def test_dec_to_bin(self):
        self.assertEqual('111', main.dec_to_bin(7))
        self.assertEqual('101', main.dec_to_bin(5))
        self.assertEqual('1101', main.dec_to_bin(13))
        self.assertEqual('11001', main.dec_to_bin(25))
        self.assertEqual('100100', main.dec_to_bin(35))
        self.assertEqual('110111', main.dec_to_bin(55))

    def test_rev_array(self):
        self.assertEqual([8, 12, 5, 20], main.rev_array([20, 5, 12, 8]))
        self.assertEqual([12, 24, 18, 2, 17, 13], main.rev_array([13, 17, 2, 18, 24, 12]))
        self.assertEqual(['bow', 'waist', 'study', 'world'], main.rev_array(['world', 'study', 'waist', 'bow']))
        self.assertEqual([True, False, True, True], main.rev_array([True, True, False, True]))

    def test_rev_string(self):
        self.assertEqual('tfihs', main.rev_string('shift'))
        self.assertEqual('ygoloib', main.rev_string('biology'))
        self.assertEqual('', main.rev_string(''))
        self.assertEqual('dlroW olleH', main.rev_string('Hello World'))
        self.assertEqual(".teerts eht no ananab yggos a dnif uoy netfo ton s'tI", main.rev_string("It's not often you find a soggy banana on the street."))

    def test_rec_fib(self):
        self.assertEqual(0, main.rec_fib(0))
        self.assertEqual(1, main.rec_fib(1))
        self.assertEqual(2, main.rec_fib(3))
        self.assertEqual(5, main.rec_fib(5))
        self.assertEqual(13, main.rec_fib(7))
        self.assertEqual(55, main.rec_fib(10))
        self.assertEqual(377, main.rec_fib(14))

if __name__ == '__main__':
    unittest.main()
