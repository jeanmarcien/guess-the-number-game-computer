'''This is a Python script to play a Guess Number Game with the computer.'''
'''The computer will randomly pick an integer between 0 and 100 and the user will try to find the number within 5 attempts.'''

import random

def verify_number(random_number, user_number, begin_point = 0, end_point = 100, trial = 1):
    while trial <= 5:
        if trial == 5:
            print(f"Game Over! Thanks for playing. The number was {random_number}.")
            break
        elif user_number < random_number:
            print(f"Sorry, the number you chose is too low. Try again.")
            begin_point = user_number
            user_number = int(input(f"Choose a new number between {begin_point} and {end_point}: "))
        elif user_number > random_number:
            print(f"Sorry, the number you chose is too high. Try again.")
            end_point = user_number
            user_number = int(input(f"Choose a new number between {begin_point} and {end_point}: "))
        else:
            print(f"Congratulations, you hit the jackpot! The number was {random_number}.")
            break
        trial += 1

random_number = random.randint(0, 100)
user_number = int(input("Choose a number between 0 and 100: "))
#print(random_number)

verify_number(random_number, user_number)
