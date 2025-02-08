PASSWORD_LENGTH =10

def main():
    """Main function"""
    password = get_password()

    get_asterisk(password)


def get_asterisk(password):
    """Get the number of asterisks"""
    length = len(password)
    print(f"{length * "*"}")


def get_password():
    """Check for valid password"""
    password = input("Enter password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Enter password: ")
    return password


main()