import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print_colored("Invalid choice. Please choose Rock, Paper, or Scissors.", Fore.RED)
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print_colored("Let's play Rock-Paper-Scissors!", Fore.CYAN)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {Fore.GREEN}{user_choice}{Style.RESET_ALL}.")
    print(f"The computer chose {Fore.RED}{computer_choice}{Style.RESET_ALL}.")

    result = determine_winner(user_choice, computer_choice)
    print_colored(result, Fore.MAGENTA)

if __name__ == "__main__":
    play_game()
