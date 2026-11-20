# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is true for odd numbers, not even numbers. For even numbers, n % 2 should equal 0.
Example: is_even(4) → False (actual), True (expected)
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but the area of a rectangle is width multiplied by height, not added.
Example: rectangle_area(5, 3) → 8 (actual), 15 (expected)
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but the docstring says "twice the number n", which means it should multiply n by 2.
Example: double(4) → 6 (actual), 8 (expected)
Fix: return n * 2
