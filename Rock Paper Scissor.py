import random


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Rock, paper, or scissors? ")
    computer_choice = random.choice(choices)

    print("You chose {}.".format(user_choice))
    print("The computer chose {}.".format(computer_choice))

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    rock_paper_scissors()
