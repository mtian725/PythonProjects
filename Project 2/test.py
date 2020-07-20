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

    def test_bubble_sort(self):
        self.assertEqual([-47, -44, -9, 20, 29], bubble_sort([20, -44, 29, -47, -9]))
        self.assertEqual([-19, -11, 23, 28, 45], bubble_sort([23, -11, -19, 28, 45]))
        self.assertEqual([-30, 14, 14, 23, 31], bubble_sort([23, 14, 31, 14, -30]))
        self.assertEqual([], bubble_sort([]))

    def test_duplicate_val(self):
        self.assertEqual(True, duplicate_val([1, 2, 3, 2, 5]))
        self.assertEqual(False, duplicate_val([7, 1, 5, 2, 8, 9]))
        self.assertEqual(True, duplicate_val([-18, -18, -30, 14, 10]))
        self.assertEqual(False, duplicate_val([32, 8, 25, 9, -47]))
        self.assertEqual(False, duplicate_val([]))

    def test_is_square_matrix(self):
        self.assertEqual(True, is_square_matrix([[1, 2, 1], [2, 1, 2], [1, 2, 1]]))
        self.assertEqual(False, is_square_matrix([[3], [2, 1], [1, 2, 1, 5]]))
        self.assertEqual(True, is_square_matrix([[3, 3], [3, 3]]))
        self.assertEqual(False, is_square_matrix([[3, 6, 4], [2], [1]]))
        self.assertEqual(True, is_square_matrix([]))

    def test_total_100(self):
        self.assertEqual(True, total_100({1: 57, 2: 17, 3:40}))
        self.assertEqual(False, total_100({1: 15, 2: 13, 3: 10}))
        self.assertEqual(False, total_100({1: 0, 2: 0, 3: 0, 4: 99}))
        self.assertEqual(True, total_100({1: -25, 2: 50, 3: 155}))
        self.assertEqual(False, total_100({1: -3, 4: -6, 10: -123}))
        self.assertEqual(False, total_100({}))

    def test_fib(self):
        self.assertEqual({1: 0}, fib(1))
        self.assertEqual({1: 0, 2: 1}, fib(2))
        self.assertEqual({1: 0, 2: 1, 3: 1, 4: 2, 5: 3}, fib(5))
        self.assertEqual({1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8}, fib(7))
        self.assertEqual({1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8, 8: 13, 9: 21, 10: 34}, fib(10))

    def test_matrix_sort(self):
        self.assertEqual([[-10, -7, -5], [-4, -2, -1], [1, 4, 7]], matrix_sort([[-10, -7, 7], [4, 1, -5], [-1, -4, -2]]))
        self.assertEqual([[-8, -8, -5], [-3, -3, -2], [8, 10, 10]], matrix_sort([[10, -8, -3], [-2, -3, -5], [8, 10, -8]]))
        self.assertEqual([], matrix_sort([]))

    def test_matrix_mult(self):
        self.assertEqual([[-2, 15], [10, 2]], matrix_mult([[1, 3],[2, -1]], [[4, 3], [-2, 4]]))
        self.assertEqual([[16, -12, -5], [4, 11, -3], [28, -11, -10]], matrix_mult([[1, 3], [2, -1], [3, 4]], [[4, 3, -2], [4, -5, -1]]))
        self.assertEqual([], matrix_mult([], []))
