MENU = """(G) - Get valid score
(P) - Print result
(S) - Show stars
(Q)uit"""
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

def main():
    print(MENU)
    choice = input(">>> ").upper()
    score = int(input("Enter score: "))

    while choice != "Q":
        if choice == "G":
            get_valid_score(score)
        elif choice == "P":
            get_result(score)
            print(get_result(score))
        elif choice == "S":
            get_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_valid_score(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        return "Invalid score"

def get_result(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT:
        return "Excellent"
    elif score >= PASSABLE:
        return "Passable"
    else:
        return "Bad"

def get_stars(score):
    print(f"{score * "*"}")


main()