# game that generates a random number and asks a user to guess it

import random  # this statement is needed because we're using functions from the 'random' library

print("I've chosen a number between zero and ten. Try to guess it!")
number = random.randrange(11)    # generates a number between 0 and 10
found = False

while not found:
    guess = int(input())    # takes input and turns it into an int
    if guess == number:
        print("Correct!")
        found = True    # this will stop the loop before the next cycle
    elif guess > number:
        print("Too high! Guess again.")
    elif guess < number:
        print("Too low! Guess again.")

# suggestions

# play the game a few times. Try to walk through the code and figure out how it works.
# try changing the range of possible numbers. Make sure to change it in the print statement too!
# try adding an if-clause for "one away"
# try choosing a number range that doesn't start at 0
