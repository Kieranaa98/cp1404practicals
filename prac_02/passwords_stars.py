PASSWORD_LENGTH =10

def main():
    password = get_password()

    length = len(password)

    print(f"{length * "*"}")


def get_password():
    password = input("Enter password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Enter password: ")
    return password


main()