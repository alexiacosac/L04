# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1.
Example: input: 4, actual result: False, expected result: True
Fix: return n % 2 == 0

Line: 8
Problem: The function incorrectly returns the sum of width and height instead of the product (area of a rectangle).
Example: input: width=5, height=3, actual result: 8, expected result: 15
Fix: return width * height

Line: 13
Problem: The function adds 2 to n instead of doubling it. It should return 2 * n.
Example: input: 5, actual result: 7, expected result: 10
Fix: return n * 2
