# Project 2
This project is going to focus on iteration, arrays, 2D arrays, and
dictionaries. You can choose whether or not to use `for` or `while` loops for
each of the tasks.

Run `python3 test.py` to test your code.

Run `python3 -v test.py` to see the results of each individual test.

To reduce visual clutter while working, I highly recommend commenting out the tests that you're not working on. (By commenting out the function definition and its contents).

Feel free to add onto test.py if you want to do more thorough testing.

Part 1: Iteration
-----------------
`def next_perfect_squares(start)`
* **Description**: Given some start number, return the next 5 perfect squares
as a string separated by spaces.
* **Examples**:
```
next_perfect_squares(0) => '1 4 9 16 25'
next_perfect_squares(50) => '64 81 100 121 144'
```

`def fizzbuzz(num)`
* **Description**: Given some number, create a string from 1 to num, where each value is separated by commas. If the number is a multiple of 3, put **Fizz**
instead. If the number is a multiple of 5, put **Buzz** instead. If the number
is a multiple of both, put **FizzBuzz**.
* **Examples**:
```
fizzbuzz(15) => '1, 2, Fizz, 4, Buzz, Fizz, 7, 8,
                Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz'
```

Part 2: Arrays and 2D Arrays
-----------------
`def bubble_sort(arr)`
* **Description**: Given an array of integers, sort the array from least to
greatest. Do this by looping through the array until it is sorted, and if there
is an element greater than the next element, swap them. This is also known as bubble sort, where the larger values "bubble" up to the end of the array.
**Do not use the sort() function for this.**
* **Examples**:
```
bubble_sort([20, -44, 29, -47, -9] => [-47, -44, -9, 20, 29]

First scan: [20, -44, 29, -47, -9] => [-44, 20, 29, -47, -9]
         => [-44, 20, -47, 29, -9] => [-44, 20, -47, -9, 29]

Second scan: [-44, 20, -47, -9, 29] => [-44, -47, 20, -9, 29]
          => [-44, -47, -9, 20, 29]

Last scan: [-44, -47, -9, 20, 29] => [-47, -44, -9, 20, 29]
```

`def duplicate_val(arr)`
* **Description**: Given an array of integers, return True if there exists two
integers that are equal. Otherwise, return False.
* **Examples**:
```
duplicate_val([1, 2, 3, 2, 5]) => True
duplicate_val([7, 1, 5, 2, 8, 9]) => False
```

`def is_square_matrix(arr)`
* **Description**: Given a 2D array of values, return True if it is a square
matrix. Otherwise, return False. A square matrix is one where the number of
columns and the number of rows are equal.
* **Examples**:
```
is_square_matrix([[1, 2, 1], [2, 1, 2], [1, 2, 1]]) => True

[[1, 2, 1],
[2, 1, 2],
[1, 2, 1]]

is_square_matrix([[3], [2, 1], [1, 2, 1, 5]]) => False
[[3],
[2, 1],
[1, 2, 1, 5]]
```

Part 3: Dictionaries
-----------------
`def total_100(dict)`
* **Description**: Given some dictionaries where all the values are integers,
return True if the sum of all those values is greater than or equal to 100.
Return False otherwise.
* **Examples**:
```
total_100({1: 57, 2: 17, 3:40}) => True
total_100({1: 15, 2: 13, 3: 10}) => False
```

`def fib(num)`
* **Description**: Given some number, return a dictionary that has that many
Fibonacci numbers.
* **Examples**:
```
fib(2) => {1: 0, 2: 1}
fib(5) => {1: 0, 2: 1, 3: 1, 4: 2, 5: 3}
```

Part 4: Challenge (Optional)
-----------------
`def matrix_sort(arr)`
* **Description**: Given a 2D array, sort it. You can assume that the matrix
will be square. You can use any sorting method, but **do not use the sort() function for this.**
* **Examples**:
```
matrix_sort([[-10, -7, 7], [4, 1, -5], [-1, -4, -2]] =>
    [[-10, -7, -5], [-4, -2, -1], [1, 4, 7]]

matrix_sort([[10, -8, -3], [-2, -3, -5], [8, 10, -8]]) =>
    [[-8, -8, -5], [-3, -3, -2], [8, 10, 10]]
```

`def matrix_mult(arr, arr)`
* **Description**: Given two 2D arrays, multiply them together. Assume that
these matrices are valid to be multiplied together. If you're unsure how the
math works, there are many resources online explaining it.
* **Examples**:
```
matrix_mult([[1, 3],[2, -1]], [[4, 3], [-2, 4]]) =>
    [[-2, 15], [10, 2]]

matrix_mult([[1, 3], [2, -1], [3, 4]], [[4, 3, -2], [4, -5, -1]]) =>4
    [[16, -12, -5], [4, 11, -3], [28, -11, -10]]
```
