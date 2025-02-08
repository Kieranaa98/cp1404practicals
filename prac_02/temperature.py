"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Main function"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_fahrenheit()
        elif choice == "F":
            get_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_celsius():
    """Convert fahrenheit to celsius"""
    fahrenheit_option = float(input(("Fahrenheit: ")))
    celsius = 5 / 9 * (fahrenheit_option - 32)
    print(f"Result: {celsius:.2f} C")


def get_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius_option = float(input("Celsius: "))
    fahrenheit = celsius_option * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()