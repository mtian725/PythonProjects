# Project 1
This project is going to focus on getting comfortable with Python's primitive types, conditionals, and debugging. Assuming that the one completing them is new to programming, the tasks are designed on the easier end

Run `python3 test.py` to test your code.

Run `python3 -v test.py` to see the results of each individual test.

Feel free to add onto test.py if you want to do more thorough testing.

Part 1: Numbers and Strings
------------------------
`def crazy_math(x, y, z)`
* **Description**: Given some x, y, z, where z =/= 0, if x is less than 5, return the difference between the product of x, y, and z and the sum of x, y, and z. Otherwise, return the sum of x and the remainder when you divide y by z.
* **Examples**:
```
crazy_math(3, 5, 1) => 6
crazy_math(5, 2, 3) => 7
```

`def str_modify(str)`
* **Description**: Given some string, take the first 5 characters and turn them into uppercase and move them to the end of the string.
* **Examples**:
```
str_modify('amazing') => 'ngAMAZI'
str_modify('Banana Bread') => 'a BreadBANAN'

```

Part 2: Debugging
-----------------
`def debugging_1()` and `def debugging_2(num):`
* **Description**: Try and fix the functions such that they work properly. Uncomment the code below the function definition. Try to fix the bugs before running the tests on your first attempt.
* **Expected outputs**:
```
debugging_1() => 32

# return True if num is a multiple of 7
debugging_2(35) => True
debugging_2(6) => False
debugging_2(-7) => True
```

Part 3: Conditionals
--------------------
`def num_prop(num)`
* **Description**: Given a number, return a string identifying whether it is even, odd, positive, negative, or zero.
* **Examples**:
```
num_prop(7) => 'Positive and Odd'
num_prop(10) => 'Positive and Even'
num_prop(0) => 'Zero'
num_prop(-3) => 'Negative and Odd'
num_prop(-6) => 'Negative and Even'
```

`def str_size(str)`
* **Description**: Given a string, depending on how long the string is, return a string in accordance to the length.
       * 'Very small' if string is **3** characters or less
       * 'Small' if string is **5** characters or less but more than **3**
       * 'Medium' if string is **7** characters or less but more than **5**
       * 'Large' if string is **10** characters or less but more than **7**
       * 'Very Long' if string is **10** characters or more
* **Examples**:
```
str_size('abc') => 'Very small'
main.str_size('apple') => 'Small'
main.str_size('spanish') => 'Medium'
main.str_size('schedule') => 'Large'
main.str_size('hippopotamus') => 'Very Long'
```

`def complex_condition(x, y, z)`
* **Description**: Given x, y, and z, which are all boolean values, return true if and only if x is false and y is false **OR** if x is false, y is true and z is true
* **Examples**:
```
complex_condition(False, False, False) => True
complex_condition(True, True, True) => False
complex_condition(False, True, True) => True
complex_condition(False, True, False) => False
```
Part 4: Challenge (Optional)
----------------
`def has_real_roots(a, b, c)`
* **Description**: Assume you are given a quadratic equation of the form `ax^2 + bx + c`. Return True if this equation has real roots. Otherwise, return False. Assume that a =/= 0.
* **Examples**:
```
has_real_roots(1,4,4) => true
has_real_roots(2,5,3) => true
has_real_roots(1,2,2) => false
```

`def roots(a, b, c)`
* **Description**: Assume you are given a quadratic equation of the form `ax^2 + bx + c`. If there are two real roots, return a string formatted as `x and y` where x and y are the two roots to the equations and x <= y. If there is one real root, return a string formatted as `z` where z is the root. If there are no real roots, return the string `No real roots`.
* **Examples**:
```
roots(1,5,6) => '-2 and -3'
roots(1,2,4) => 'No real roots'
roots(1,10,25) => '-5'
```
