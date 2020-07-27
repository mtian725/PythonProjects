# Project 3
This project is going to focus on recursion.

Run `python3 test.py` to test your code.

Run `python3 -v test.py` to see the results of each individual test.

To reduce visual clutter while working, I highly recommend commenting out the tests that you're not working on. (By commenting out the function definition and its contents).

Feel free to add onto test.py if you want to do more thorough testing.

Functions to implement
-----------------
`def basic_recurrence(num)`
* **Description**: Given some num implement this recurrence equation. Num will
always be greater than or equal to 0.
```
f(num) = 3 * f(num - 1) + 5
f(0) = 2
```
* **Examples**
```
basic_recurrence(1) => 11
basic_recurrence(3) => 119
```

`def dec_to_bin(dec)`
* **Description**: Given some decimal number (base 10 number) convert it into
binary value, which is a string. Steps to convert decimal to binary is:
```
Divide the number by 2.
Get the integer quotient for the next iteration.
Get the remainder for the binary digit.
Repeat the steps until the quotient is equal to 0.
```
See https://www.rapidtables.com/convert/number/decimal-to-binary.html for
examples.
* **Examples**:
```
bin_to_dec(7) => '111'
bin_to_dec(5) => '101'
```

`def rev_array(arr)`
* **Description**: Given some array, reverse it.
* **Example**:
```
rev_array([20, 5, 12, 8]) => [8, 12, 5, 20]
rev_array([13, 17, 2, 18, 24, 12]) => [12, 24, 18, 2, 17, 13]
```

`def rec_fib(num)`
* **Description**: Given some num, find that Fibonacci number recursively.
* **Example**:
```
rec_fib(0) => 0
rec_fib(1) => 1
rec_fib(3) => 2
```
