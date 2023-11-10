import random

def guessing_game(difficulty):
    number_range = 100
    guesses_allowed = 5

    if difficulty == "easy":
        number_range = 50
        guesses_allowed = 10
    elif difficulty == "medium":
        number_range = 100
        guesses_allowed = 5
    elif difficulty == "hard":
        number_range = 1000
        guesses_allowed = 3

    number = random.randint(1, number_range)

    while True:
        guess = input("Guess a number between 1 and {}: ".format(number_range))
        guess = int(guess)

        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        guesses_remaining = guesses_allowed - 1

        if guesses_remaining == 0:
            print("Sorry, you ran out of guesses. The number was {}.".format(number))
            break

guessing_game("hard")
