# Bug reports for exercise3.py

Line: 3
Problem: The function averages a list but does not handle the case of an empty list as specified in the docstring. When the list is empty, `len(numbers)` will be 0, leading to a division by zero error.
Example: input: [], actual output: ZeroDivisionError, expected output: 0
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The function returns the first word of the text, but if the text is empty or contains only whitespace, `split()` returns an empty list, and accessing `[0]` will raise an IndexError.
Example: input: "   ", actual output: IndexError, expected output: ""
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: The function calculates percent but does not handle the case where total is 0 as specified in the docstring. If total is 0, dividing by zero will raise a ZeroDivisionError.
Example: input: (5, 0), actual output: ZeroDivisionError, expected output: 0
Fix: return part / total * 100 if total != 0 else 0
