import csv
from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")

    guitars.sort()

    print("\nGuitars (by year):")
    display_guitars(guitars)

    get_new_guitars(guitars)

    save_guitars("guitars.csv", guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return guitars

def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def get_new_guitars(guitars):
    """Prompt the user to enter new guitars and add them to the list."""
    name = input("Enter guitar name (or press enter to stop): ")
    while name:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar name (or press enter to stop): ")

def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)


main()
