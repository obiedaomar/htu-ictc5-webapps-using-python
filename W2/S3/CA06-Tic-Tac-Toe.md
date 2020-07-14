# CA06 - Python Basics - Review 2

## Tic-Tac-Toe

1. Start by deciding how you will store the player's marker positions (Xs and Os). Imagine the game board and assign numbers to the board.
   1. Which data structure is good for this?
   2. Use the index to keep track of your board cells.

2. Create a list called `board` which will keep track of the player markers.
   1. The list should already be the same length as your intended board.

3. Create a function `print_board(board)` that will print a board. Remember this function will be used to print the game board after every move. Try to make it pretty!

4. Write a function `make_move(marker, position)` which takes an input marker string 'X' or "O' and a given number and stores it to a list at that appendix.

5. Take a look at the `input()` function to read input from the user.
   1. Read [this](https://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python-3)

6. Write a function that takes in the board and a player marker and checks if there is a win or a tie.
   1. How would you check this?
   2. When do I run this?

7. Check for a tie (nobody won and the board list is full!)

8. Think about how to start the game.
   1. Which functions do you need to call?
   2. For example, a function which asks for a player's move, then updates the board,then checks for a win, then prints out the board.

9. How can you keep the game continually running?
   1.  A while loop can help.
   2.  Check for the game status flag, that always has the updated game status.
       1.  For example `is_running`?

10. Make sure you cast data types properly and test your code with different input.

## Solutions

You can find suggested solutions to the problems above [here](./CA06-solutions/).