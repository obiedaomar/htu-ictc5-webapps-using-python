# PA02 - Python Basics

	Course: Web Application Development Using Python (ICTC5)
	Instructor: George Khoury
	Revision: 3
	Last updated: 21-07-2020
	Submission Date: 26-07-2020 10:00am


## Submission

* Create a file `PA02_{LASTNAME}_{FIRSTINITIAL}.py` and write a solution for the problem below.
* Submit your files on **Microsoft Teams** under **Assignments**.
  * Remember to click the `Turn in` button.
* Try to document your code properly :).
* Try to adhere to the Python language conventions.

## Fruitman

For this practical assignment you will be building a hangman game, but with fruits. You are provided a text file with some words you can use to run the game. The objective of building this game is to boost your programming skills and understanding of programming logic.

The Fruitman program randomly selects a fruit from a list of secret `fruits`. You can use `fruit = random.choice(fruits).upper()` to select a random fruit for your game.

### The game

 After the random `fruit` is chosen from the collection, the player has `len(fruit)` chances to guess the fruit. After every guess entered by the user, the correctly guessed letters are printed. For every letter that is not yet guessed you can print `_` instead.

### Functions

In this section I am going to list additional function signatures you *may* need. *Depending on how you design your code, you may not need the function signatures below!*

* start_game() - starts the game
* print_fruit() - prints the current state of the fruit (all visible, all hidden letters)
* print_info() - prints the information for the current game
  * number of guesses?, how many letters?, etc.
* check_guess() - checks a guesses provided by the user
* read_fruits_list() - returns a list of fruits read from the file

### Additional ideas to implement

* Ask the user for their name and greet them afterwards.
* Provide the user the option to choose the game difficulty 
  * `Hint: add more guesses based on the difficulty level?`


