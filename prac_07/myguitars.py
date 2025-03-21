from guitar import Guitar
from prac_06.guitar import CURRENT_YEAR, VINTAGE_AGE

def main():
    guitars = []

    # Sample guitar data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Fender Stratocaster", 1954, 12345.67))
    guitars.append(Guitar("Yamaha FG800", 2016, 299.99))
    guitars.append(Guitar("Martin D-28", 1931, 3500.00))
    guitars.append(Guitar("Gibson SG", 1961, 1400.00))

    guitars.sort()

    print("\nSorted Guitars (by year):")
    display_guitars(guitars)


def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)

main()