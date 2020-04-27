# # Rock Paper Scissors
#
# This exercise will simulate a simple rock-paper-scissors game.
# Goals:
# * Request user for input
# 	* Validate input
# * Generate random choice
# * Compare and return result
# * Ask to play again


#################
#-- Data code --#
#################
import random

######################
#-- Processing code--#
######################
def start_game():
    play_again = True
    while play_again == True:
        correct_value = True
        #get users play
        while correct_value:
            str_user_play = str(input("\nWhat will it be? rock, paper, or scissor?: ")).lower()
            if str_user_play != 'rock' and str_user_play != 'paper' and str_user_play != 'scissor':
                print('Seems like you input the wrong value. Try Again.\n')
                continue
            else:
                break

        #get computers play
        int_computer_random = random.randint(1,3)
        if int_computer_random == 1:
            str_computer_play = 'rock'
        elif int_computer_random == 2:
            str_computer_play = 'paper'
        elif int_computer_random == 3:
            str_computer_play = 'scissor'
        else:
            print("Looks like something went wrong")

        champion_text = '''
                       88                                                    88                          
                       88                                                    ""                          
                       88                                                                                
             ,adPPYba, 88,dPPYba,  ,adPPYYba, 88,dPYba,,adPYba,  8b,dPPYba,  88  ,adPPYba,  8b,dPPYba,   
            a8"     "" 88P'    "8a ""     `Y8 88P'   "88"    "8a 88P'    "8a 88 a8"     "8a 88P'   `"8a  
            8b         88       88 ,adPPPPP88 88      88      88 88       d8 88 8b       d8 88       88  
            "8a,   ,aa 88       88 88,    ,88 88      88      88 88b,   ,a8" 88 "8a,   ,a8" 88       88  
             `"Ybbd8"' 88       88 `"8bbdP"Y8 88      88      88 88`YbbdP"'  88  `"YbbdP"'  88       88  
                                                                 88                                      
                                                                 88        
        '''
        loser_text = '''
            88                                              
            88                                              
            88                                              
            88  ,adPPYba,  ,adPPYba,  ,adPPYba, 8b,dPPYba,  
            88 a8"     "8a I8[    "" a8P_____88 88P'   "Y8  
            88 8b       d8  `"Y8ba,  8PP""""""" 88          
            88 "8a,   ,a8" aa    ]8I "8b,   ,aa 88          
            88  `"YbbdP"'  `"YbbdP"'  `"Ybbd8"' 88    
        '''

        #compare user against computer
        #1 rock, 2 paper, 3 scissor
        if  str_user_play == str_computer_play:
            print("You played ", str_user_play, 'and your opponent played ', str_computer_play, ' as well. Tie!')
        elif str_user_play == 'rock' and str_computer_play == 'paper':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. Dang you lost!\n', loser_text)
        elif str_user_play == 'rock' and str_computer_play == 'scissor':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. You won! You are a champion!\n', champion_text)

        elif str_user_play == 'paper' and str_computer_play == 'scissor':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. Dang you lost!\n', loser_text)
        elif str_user_play == 'paper' and str_computer_play == 'rock':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. You won! You are a champion!\n', champion_text)

        elif str_user_play == 'scissor' and str_computer_play == 'rock':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. Dang you lost!\n', loser_text)
        elif str_user_play == 'scissor' and str_computer_play == 'paper':
            print("You played", str_user_play, 'and your opponent played', str_computer_play, '. You won! You are a champion!\n', champion_text)
        else:
            print('something went wrong in the comparison')

        try_again = str(input("\n Want to play again (yes or no)?:")).lower()
        if try_again == 'yes':
            continue
        else:
            print("Thanks for playing")
            break





##############################
#-- Presentation (I/0) code--#
##############################
print("\nWelcome to the national championships of rock paper and scissors!")
str_start = input("Are you ready to get started (yes or no)?: ").lower()
if str_start == 'yes':
    start_game()
else:
    print("Maybe next time :)")
