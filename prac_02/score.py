"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

score = float(input("Enter score: "))
if score < LOWEST_SCORE or score > HIGHEST_SCORE:
    print("Invalid score")
elif score >= EXCELLENT:
    print("Excellent")
elif score >= PASSABLE:
    print("Passable")
else:
    print("Bad")