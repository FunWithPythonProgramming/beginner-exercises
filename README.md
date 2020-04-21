# beginner-exercises
This repository contains several simple beginner python exercises that can be done with very little python knowledge

## Guess The Number
The goal of this app is to play a game with the computer where you are to guess a random number and the computer will respond if it is higher, lower, or correct

### Requirements
* User is informed the starting and ending numbers (inclusive)
* User is repeatedly asked to guess until they get the number correct
* If number is lower than guess, say to guess lower
* If number is higher than guess, say to guess higher
* If number is same as the guess, congralute the user and ask if they want to play again (validate input to be binary)
* Generate statistics on games played, how many times the user won, average amount of guesses, etc 
** Store this in some way that can be outputted and read back in
** You should be able to start the game with an input file and continue with the given statistics


## Password Generator
The goal of this app is to create a random password for a user so they don't need to think of generating one themselves for new apps

### Requirements
* User should be asked for what criteria this should fulfill
** Upper Letters
** Lower Letters
** Numbers
** Special Characters
* User should be asked how many passwords they want to generate (and link each one to an application)
* Store the passwords in some output file
** Make sure we can read from a password file to see previously stored passwords
* User should be able to query for a password given an application
** Stretch: Store username too

## Rock Paper Scissors
The goal of this app is to play a rock paper scissors game with the computer and get a result on who won. It should also support multiple games

### Requirements
* User should be prompted for a choice (this should be validated)
* Computer randomly picks a choice
* Computer determines who won
** Give specific message depending on who won
* Computer should ask if the user wants to play again
* Once user finishes game, they should be given statistics on how many games played / won
    * Store this in some way that can be outputted and read back in
    * You should be able to start the game with an input file and continue with the given statistics

