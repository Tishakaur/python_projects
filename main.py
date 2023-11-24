import random

while True:
    player_choice = input("Enter a choice (rock , paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choice)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


