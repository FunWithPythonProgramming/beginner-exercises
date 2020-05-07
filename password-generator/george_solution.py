import random
import math
import string

def create_password():
    lower_letters = ",".join(string.ascii_lowercase)
    upper_letters = ",".join(string.ascii_uppercase)
    numbers = [str(number+1) for number in range(9)]
    symbols = ",".join(string.punctuation)

    # check if it actually is >= 4
  
    while True:
        password_length = int(input("How long should the password be? (must be greater than 4) "))
        if password_length <=  4:
            print("More than 4 doofus")
        else:
            break
    condition_count = 0
    
    need_letters = input("letters? (y/n) ").lower()
    if need_letters:
        need_upper_letters = input("upper? (y/n) ").lower()
        if need_upper_letters in ("y", "yes"):
            condition_count += 1
        need_lower_letters = input("lower? (y/n) ").lower()
        if need_lower_letters in ("y", "yes"):
            condition_count += 1

    need_numbers = input("numbers? (y/n) ").lower()
    if need_numbers in ("y", "yes"):
            condition_count += 1
    need_symbols = input("symbols? (y/n) ").lower()
    if need_symbols in ("y", "yes"):
            condition_count += 1
   
    min_of_each = math.ceil(password_length / condition_count)
    # if this isn't a multiple of 4, this will be wrong
    sub_num = (password_length - (min_of_each*condition_count))
    password = ""
    data_folder = []
    for number in range(min_of_each):
        if need_letters in ("y", "yes"):
            if need_upper_letters in ("y", "yes"):
                password += random.choice(upper_letters)
            if need_lower_letters in ("y", "yes"):
                password += random.choice(lower_letters)
        if need_numbers in ("y","yes"):
            password += random.choice(numbers)
        if need_symbols in ("y","yes"):
            password += random.choice(symbols)
    data_folder.append(password[:sub_num])
    return password[:sub_num]



def main():
    number_of_passwords = int(input("How many passwords should I create? "))
    for _ in range(number_of_passwords):
        print(create_password())

main()