import random

def create_password():
    lower_letters = ("a", "b", "c", "d")
    upper_letters = ("A", "B", "C", "D")
    numbers = [str(number+1) for number in range(9)]
    symbols = ["!", "@", "#", "$", "%"]

    password_length = int(input("How long should the password be? (must be greater than 4) "))
    # check if it actually is >= 4
    condition_count = 0
    
    need_letters = input("letters? (y/n) ")
    if need_letters:
        need_upper_letters = input("upper? (y/n) ")
        if need_upper_letters == "y":
            condition_count += 1
        need_lower_letters = input("lower? (y/n) ")
        if need_lower_letters == "y":
            condition_count += 1

    need_numbers = input("numbers? (y/n) ")
    if need_numbers == "y":
            condition_count += 1
    need_symbols = input("symbols? (y/n) ")
    if need_symbols == "y":
            condition_count += 1
    
    min_of_each = password_length // condition_count
    # if this isn't a multiple of 4, this will be wrong
    password = ""
    for number in range(min_of_each):
        if need_letters == "y":
            if need_upper_letters == "y":
                password += random.choice(upper_letters)
            if need_lower_letters == "y":
                password += random.choice(lower_letters)
        if need_numbers == "y":
            password += random.choice(numbers)
        if need_symbols == "y":
            password += random.choice(symbols)

    return password



def main():
    number_of_passwords = int(input("How many passwords should I create? "))
    for _ in range(number_of_passwords):
        print(create_password())

main()