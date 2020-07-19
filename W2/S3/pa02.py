# Fruitman

import random

#
# Global variables
#

wrong = 0
correct = 0
max_tries = 0  # How many guesses does the player get?

fruits = []      # The list of fruits to choose from
fruit = ""       # The fruit for this round
fruit_guessed = False

letters_guessed = ''  # Letters guess so far

#
# Functions
#

# get_fruit()


def get_fruit():
    global fruits
    global fruit

    fruits = open("fruits.txt", "r").read().split(" ")
    fruit = random.choice(fruits).upper()

# ask_for_guess()


def ask_for_guess():
    global max_tries
    while (max_tries != 0) and fruit_guessed is False:
        try:
            max_tries -= 1
            return str(input('Enter a letter to guess: ')).upper()[0]
        except:
            print('Enter only a letter!')
            continue

# check_guess()


def check_guess(guess):
    global letters_guessed
    # If letter is guessed correctly
    if guess in fruit:
        # count the number of occurences
        c = fruit.count(guess)
        for _ in range(c):
            letters_guessed += guess  # add the number of the occurences to 'letters_guessed'

# setup_game()


def setup_game():
    global max_tries

    # Load list of fruits and choose a fruit at random
    get_fruit()
    max_tries = len(fruit)   # Set max_tries

    # Print game information to the player
    print(f"You need to guess a {len(fruit)} letter fruit.")
    print(f"You have {max_tries} guesses.")

    # Print the masked fruit
    for _ in fruit:
        # For printing the empty spaces for letters of the fruit
        print('_', end=' ')
    print()

# print_fruit()


def print_fruit():
    global correct
    global letters_guessed

    for char in fruit:
        # Print the char if the user guessed it
        if char in letters_guessed and (len(letters_guessed) != len(fruit)):
            print(char, end=' ')
            correct += 1
        # Print all characters if the user guessed the fruit
        elif (len(letters_guessed) == len(fruit)):
            end_game("won", max_tries, fruit)
            break  # To break out of the for loop
        # Print '_' for each unguessed letter
        else:
            print('_', end=' ')

# end_game()


def end_game(status, tries, fruit):
    global fruit_guessed

    if status is "won":
        fruit_guessed = True
        print('\n\nYou won!')
        print(f'It took you {tries} to guess the fruit {fruit}.')
    else:
        print('\n\nYou lost!')
        print(f'The fruit was "{fruit}".')

# start_game()


def start_game():
    global max_tries

    # While player has tries and fruit has not been guessed
    while (max_tries != 0) and fruit_guessed is False:
        print()

        # Ask user for guess
        guess = ask_for_guess()

        # Check guess
        check_guess(guess)

        # Print the fruit
        print_fruit()

        # If user has used all of his chances
        if max_tries <= 0 and (len(letters_guessed) != len(fruit)):
            end_game("lost", 0, fruit)

#
# Main
#


print("\n----- Welcome to FRUITMAN, try to guess the mystery fruit -----\n")

setup_game()
start_game()
