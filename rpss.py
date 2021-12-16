#!/usr/bin/env python3
from random import randint

t = ["Rock", "Paper", "Scissors", "Shoot"]

computer = t[randint(0,3)]

still_playing = False

while still_playing == False:
    player_choice = input("Rock, Paper, Scissors, Shoot? ")
    if player_choice == computer:
        print("Tie!")
    elif player_choice == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player_choice)
        else:
            print("You win!", player_choice, "smashes", computer)
    elif player_choice == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player_choice)
        else:
            print("You win!", player_choice, "covers", computer)
    elif player_choice == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player_choice)
        else:
             print("You win!", player_choice, "cut", computer)
    elif player_choice == "Shoot":
        if computer == "Scissors":
            print("You lose!", computer, "Got you first", player_choice)
        else:
            print("You win!", player_choice, "knife to a gun fight", computer)
else:
    print("invalid play. Try again!")
    
    still_playing = False
    computer = t[randint(0,3)]

