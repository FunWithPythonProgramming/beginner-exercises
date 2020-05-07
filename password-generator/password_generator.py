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
    numbers = [str(number+1) for number in range(10)]
    symbols = ["!", "@", "#", "$", "%"]

    while True:
        try:
            password_length = int(input("How long should the password be? (must be greater than or equal to 4) "))
            if password_length < 4:
                while True:
                    password_length = int(input("Password (must be greater than or equal to 4) "))
                    if password_length < 4:
                        continue
                    else:
                        break
                if password_length >= 4:
                    break
            else:
                break
        except ValueError as error:
            print("Input must be a whole number, please do not type any strings/characters\n")

    if password_length > 3:
    # check if it actually is >= 4
        condition_count = 0

        while True:
            need_letters = input("letters? (y/n) ")
            if need_letters.lower().strip() not in ('y', 'n'):
                print("please type 'y' or 'n' when prompted with question again")
            else:
                break
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

        for number in range(password_length):
            if need_letters.strip().lower() == "y":

                if need_upper_letters.strip().strip() == "y":
                    password += random.choice(upper_letters)

                if need_lower_letters.strip().lower() == "y":
                    password += random.choice(lower_letters)

            if need_numbers.strip().strip() == "y":
                password += random.choice(numbers)

            if need_symbols.strip().strip() == "y":
                password += random.choice(symbols)

        return password

def number_of_passwords():
    while True:
        try:
            number_of_passwords = int(input("How many passwords should I create? "))
            return number_of_passwords
        except ValueError as error:
            print("Please return a whole number or you will be stuck in an infinite loop\n")

def main():
    num_password = number_of_passwords()
    pwd = ""
    for _ in range(num_password):
        print(create_password())
        pwd += create_password()
    return pwd

    
with open("password.txt", 'w') as pwd_txt:
    passwords = main()
    print(passwords)
    for line in passwords:
        data = pwd_txt.write(line)

