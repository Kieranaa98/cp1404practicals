MENU = """(G) - Get valid score
(P) - Print result
(S) - Show stars
(Q)uit"""
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

def main():
    """Main function"""
    print(MENU)
    choice = input(">>> ").upper()
    score = get_valid_score()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            get_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_valid_score():
    """Get a valid score from user input"""
    score = int(input("Enter score: "))
    while score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def get_result(score):
    """Determine the result of the score"""
    if score >= EXCELLENT:
        return "Excellent"
    elif score >= PASSABLE:
        return "Passable"
    else:
        return "Bad"

def get_stars(score):
    """Print the number of asterisks according to score"""
    print("*" * score)

main()
