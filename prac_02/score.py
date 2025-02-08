"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

def main():
    score = float(input("Enter score: "))
    print(get_result(score))

    random_score = random.randint(LOWEST_SCORE,HIGHEST_SCORE)
    print(random_score)
    print(get_result(random_score))

def get_result(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT:
        return "Excellent"
    elif score >= PASSABLE:
        return "Passable"
    else:
        return "Bad"


main()