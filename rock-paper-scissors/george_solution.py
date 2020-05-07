import random



def play_game(choice):
    choices = ["rock", "paper", "scissor"]
    comp_choice = choices[random.randint(0,2)]
    player_choice = str(choice).lower() 
    while True:
        if player_choice == comp_choice:
            print(f"Its a draw ..{player_choice} vs {comp_choice}!!")
            return
        elif player_choice == "rock" and comp_choice == "paper":
            print(f"You lose...{player_choice} gets covered by {comp_choice}")
            return   
        elif player_choice == "rock" and comp_choice == "scissor":
            print(f"You win...{player_choice} smashes {comp_choice}")
            return
        elif player_choice == "scissor" and comp_choice == "paper":
            print(f"You win...{player_choice} cuts {comp_choice}")
            return
        elif player_choice == "scissor" and comp_choice == "rock":
            print(f"You lose...{player_choice} gets smashed by {comp_choice}")
            return
        elif player_choice == "paper" and comp_choice == "rock":
            print(f"You win ...{player_choice} covers {comp_choice}")
            return
        elif player_choice == "paper" and comp_choice == "scissor":
            print(f"You lose...{player_choice} gets cut by {comp_choice}")
            return
        else:
            print("Please enter rock, paper, or scissor")
        
def main():
    
    
    choice = str(input("Choose rock, paper, or scissor:  "))
    play_game(choice)
    play_again = True
    while play_again:
        play_again_input = input("Do you want to play again (y/n)? ").lower()
        while play_again_input not in ("y", "n"): 
            play_again_input = input("Invalid Answer, Please Type 'y' or 'n'? ").lower()
        if play_again_input == "n":
            print("OK ...BYE BYE!!")
            return
        else:
            main ()

if __name__ == "__main__":
    main()
   


# # guess the number
# import random
# def play_game(max_number):
#     random_number = random.randint(0, max_number)
#     guess = int(input(f"Guess A Number Between 0 and {max_number}: "))
#     count = 1
#     while True:
#         if guess > random_number:
#             guess = int(input("Too High! Guess Again: "))
#             count += 1
#         elif guess < random_number:
#             guess = int(input("Too Low! Guess Again: "))
#             count += 1 
#         else:
#             print(f"You Got It In {count} Guesses!")
#             return count
# def main():
#     guesses = []
#     play_again = True
#     while play_again:
#         max_number = int(input("Pick a max number: "))
#         guesses.append(play_game(max_number))
#         play_again_input = input("Do you want to play again (y/n)? ").lower()
#         while play_again_input not in ("y", "n"): 
#             play_again_input = input("Invalid Answer, Please Type 'y' or 'n'? ").lower()
#         if play_again_input == "n":
#             print(f"The Max Number Of Guesses Was: {max(guesses)}")
#             print(f"The Min Number Of Guesses Was: {min(guesses)}")
#             print(f"The Average Number Of Guesses Was: {sum(guesses)/len(guesses)}")
#             return
#         else:
#             continue
# if __name__ == "__main__":
#     main()