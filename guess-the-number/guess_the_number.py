# guess the number

import random

def parse_int_from_input(input_question):
    while True:
        try:
            return int(input(input_question))
        except ValueError:
            print("Pick A Valid Integer")

def play_game(max_number):
    random_number = random.randint(0, max_number)
    guess = parse_int_from_input(f"Guess A Number Between 0 and {max_number}: ")
    count = 1

    while True:
        if guess > random_number:
            guess = parse_int_from_input("Too High! Guess Again: ")
            count += 1
        elif guess < random_number:
            guess = parse_int_from_input("Too Low! Guess Again: ")
            count += 1 
        else:
            print(f"You Got It In {count} Guesses!")
            return count

def main():
    guesses = []
    play_again = True
    while play_again:
        max_number = parse_int_from_input("Pick a max number: ")
        guesses.append(play_game(max_number))

        play_again_input = input("Do you want to play again (y/n)? ").lower()
        while play_again_input not in ("y", "n"): 
            play_again_input = input("Invalid Answer, Please Type 'y' or 'n'? ").lower()
        
        if play_again_input == "n":
            print(f"The Max Number Of Guesses Was: {max(guesses)}")
            print(f"The Min Number Of Guesses Was: {min(guesses)}")
            print(f"The Average Number Of Guesses Was: {average(guesses)}")
            break
        else:
            continue

if __name__ == "__main__":
    main()
