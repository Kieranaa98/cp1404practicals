import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Line 1. Smallest possible number is 5 and the largest is 20.
Line 2. Smallest possible number is 3 and no line 2 cannot produce 4.
Line 3. Smallest possible number is 2.5 and the largest is 5.5.
"""
