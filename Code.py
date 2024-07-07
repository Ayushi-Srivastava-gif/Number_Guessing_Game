#Guess Number Game

import random

def playgame():
    is_game_over=False
    print("Welcome to the number guessing game!.\n I'm thinking of a number between 1 and 100?")
    number=random.randint(1,100)
    # print(f"psst the number is {number}")

    abc=input("Choose the difficulty: 'easy' or 'hard'.").lower()

    attempts= 10 if abc=='easy'else 5

    while not is_game_over:
        for i in range(attempts):
            num=int(input ("Guess the number:\n"))
            if num>number:
                print("To High")
            elif num<number:
                print("To low")
            else:
                is_game_over=True
                print("congratulations! You have guessed the correct number")
                break
        else:
            is_game_over=True
            print("You have used all your attempts.You lose")
        
while input("Do you wanna play a game? Type 'y' or 'n'.").lower() =='y':
    playgame()