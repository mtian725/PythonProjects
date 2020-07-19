import main
import unittest

class TestProject2(unittest.TestCase):

if __name__ == '__main__':
    def test_next_perfect_squares(self):
        self.assertEqual('1 4 9 16 25', next_perfect_squares(0))
        self.assertEqual('64 81 100 121 144', next_perfect_squares(50))
        self.assertEqual('49 64 81 100 121', next_perfect_squares(37))
        self.assertEqual('25 36 49 64 81', next_perfect_squares(17))
        self.assertEqual('1 4 9 16 25', next_perfect_squares(-18))

    def test_fizzbuzz(self):
        self.assertEqual('1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz', fizzbuzz(10))
        self.assertEqual('1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, '+
                '11, Fizz, 13, 14, FizzBuzz', fizzbuzz(15))
        self.assertEqual('1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, '+
                '11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, '+
                'Fizz, 22, 23, Fizz, Buzz', fizzbuzz(25))
        self.assertEqual('1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, '+
                '11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, '+
                'Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, '+
                '31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, '+
                '41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, ', fizzbuzz(50))
        self.assertEqual('1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, '+
                '11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, '+
                'Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, '+
                '31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, '+
                '41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, '+
                'Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, '+
                '61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, '+
                '71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz, '+
                'Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz, '+
                '91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz', fizzbuzz(100))
