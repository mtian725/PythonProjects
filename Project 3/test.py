import main
import unittest

class TestProject3(unittest.TestCase):

if __name__ == '__main__':
    def test_basic_recurrence(self):
        self.assertEqual(2, basic_recurrence(0))
        self.assertEqual(11, basic_recurrence(1))
        self.assertEqual(119, basic_recurrence(3))
        self.assertEqual(1091, basic_recurrence(5))

    def test_dec_to_bin(self):
        self.assertEqual('111', bin_to_dec(7))
        self.assertEqual('101', bin_to_dec(5))
        self.assertEqual('1101', bin_to_dec(13))
        self.assertEqual('11001', bin_to_dec(25))
        self.assertEqual('100100', bin_to_dec(35))
        self.assertEqual('110111', bin_to_dec(55))

    def test_rev_array(self):
        self.assertEqual([8, 12, 5, 20], rev_array([20, 5, 12, 8]))
        self.assertEqual([12, 24, 18, 2, 17, 13], rev_array([13, 17, 2, 18, 24, 12]))
        self.assertEqual(['bow', 'waist', 'study', 'world'], rev_array(['world', 'study', 'waist', 'bow']))
        self.assertEqual([True, False, True, True], rev_array([True, True, False, True]))

    def test_rev_string(self):
        self.assertEqual('tfihs', rev_string('shift'))
        self.assertEqual('ygoloib', rev_string('biology'))
        self.assertEqual('', rev_string(''))
        self.assertEqual('dlroW olleH', rev_string('Hello World'))
        self.assertEqual(".teerts eht no ananab yggos a dnif uoy netfo ton s'tI", rev_string("It's not often you find a soggy banana on the street."))

    def test_rec_fib(self):
        self.assertEqual(0, rec_fib(0))
        self.assertEqual(1, rec_fib(1))
        self.assertEqual(2, rec_fib(3))
        self.assertEqual(5, rec_fib(5))
        self.assertEqual(13, rec_fib(7))
        self.assertEqual(55, rec_fib(10))
        self.assertEqual(377, rec_fib(14))
