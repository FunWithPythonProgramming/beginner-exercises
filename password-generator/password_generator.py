""""
The goal of this exercise is to create a new random password that can be used as credentials online. Goals:

    User has the choice to query/create passwords
    Request user for number of passwords to generate
        For each password, user has to specify an application and username
    Request user for requirements
        letters
        upper case
        lower case
        numbers
        symbols)
        size (length of password)
    Return password that fulfills all requirements
    Store the passwords in an output file
    Read passwords from an input file
"""


import random
import string

def create_password():
    lower_letters = tuple(string.ascii_lowercase)
    upper_letters = tuple(string.ascii_uppercase)
    numbers = [str(number) for number in range(10)] # 0..9
    symbols = tuple(string.punctuation)

    application_name = input("What application is this password for? ").lower().strip()

    while True:
        try:
            password_length = int(input("How long should the password be? (must be greater than or equal to 4) "))
            if password_length >= 4:
                break
            else:
                raise ValueError("Password Length Mus Be >= 4")
        except ValueError as error:
            print("Input must be a whole number and >= 4, please do not type any strings/characters\n")
    
    condition_count = 0

    while True:
        need_letters = input("letters? (y/n) ")
        if need_letters.lower().strip() not in ('y', 'n'):
            print("please type 'y' or 'n' when prompted with question again")
            continue
        if need_letters.strip().lower() == 'y':
            while True:
                need_upper_letters = input("upper? (y/n) ")
                if need_upper_letters.lower().strip() not in ('y', 'n'):
                    print("please type 'y' or 'n' when prompted with question again")
                else:
                    break

            if need_upper_letters.lower().strip() == "y":
                condition_count += 1

            while True:
                need_lower_letters = input("lower? (y/n) ")
                if need_lower_letters.lower().strip() not in ('y', 'n'):
                    print("please type 'y' or 'n' when prompted with question again")

                else:
                    break

            if need_lower_letters.lower().strip() == "y":
                condition_count += 1

        while True:
            need_numbers = input("numbers? (y/n) ")
            if need_numbers.lower().strip() not in ('y', 'n'):
                print("please type 'y' or 'n' when prompted with question again")

            else:
                break

        if need_numbers.strip().lower() == "y":
                condition_count += 1

        while True:
            need_symbols = input("symbols? (y/n) ")

            if need_symbols.lower().strip() not in ('y', 'n'):
                print("please type 'y' or 'n' when prompted with question again")

            else:
                break

        if need_symbols.lower().strip() == "y":
                condition_count += 1

        min_of_each = password_length // condition_count
        # if this isn't a multiple of 4, this will be wrong
        password = ""

        for number in range(min_of_each):
            if need_letters.strip().lower() == "y":

                if need_upper_letters.strip().strip() == "y":
                    password += random.choice(upper_letters)

                if need_lower_letters.strip().lower() == "y":
                    password += random.choice(lower_letters)

            if need_numbers.strip().strip() == "y":
                password += random.choice(numbers)

            if need_symbols.strip().strip() == "y":
                password += random.choice(symbols)

        return (application_name, password)

def number_of_passwords():
    while True:
        try:
            return int(input("How many passwords should I create? "))
        except ValueError as error:
            print("Please return a whole number or you will be stuck in an infinite loop\n")

def create_passwords():
    num_password = number_of_passwords()
    passwords = {}
    for _ in range(num_password):
        application_name, password = create_password()
        print(application_name, password)
        passwords[application_name] = password
    return passwords

def query_password(password_dict):
    if not password_dict:
        print("No passwords to search through!")
    else:
        while True:
            print("Application List: ")
            for application_name in password_dict:
                print(application_name)
            application_name = input("Which application password would you like? ").lower().strip()
            password = password_dict.get(application_name)
            if password:
                print(password)
                break
            else:
                print("This application doesn't exist, try again")


def export_passwords(password_dict):
    file_name = input("What file should I export this to? ")
    with open(file_name, 'w') as password_txt:
        for application in password_dict:
            data = password_txt.write(f"{application}, {password_dict[application]}\n")


def import_passwords()
    file_name = input("What file should I import from? ")


def main():
    passwords = {}
    while True:
        print("Options: \n1. Import Passwords\n2. Create Passwords\n3. Query Password\n4. Export Passwords\n5. Exit")
        command = 0
        while command not in (1, 2, 3, 4, 5):
            command = validate_integer_input("What would you like to do: ")
        
        if command == 1:
            import_password(file_name)
        elif command == 2:
            passwords.update(create_passwords())
        elif command == 3:
            query_password(passwords)
        elif command == 4:
            export_passwords(passwords)
        else:
            break


def validate_integer_input(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please enter a valid integer")


if __name__ == "__main__":
    main()
