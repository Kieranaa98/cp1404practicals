"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If input is not an integer.

2. When will a ZeroDivisionError occur?
If either input is a zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Have an error checking that prevents the uses from inputting the value zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")