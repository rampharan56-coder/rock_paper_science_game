import random

OPTIONS = ("rock", "paper", "scissor")
BEATS = {"rock": "scissor", "scissor": "paper", "paper": "rock"}

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in OPTIONS:
            return choice
        print("Invalid choice. Please choose rock, paper, or scissors.")
        
def main():
    while True:
        user = get_user_choice()
        computer = random.choice(OPTIONS)
        print(f"Computer chose {computer}.")
        
        if user == computer:
            print("It's a tie")
        elif BEATS[user] == computer:
            print("You win!")
        else:
            print("You lose!")
        
        if input("Play again? (yes/no): ").strip().lower() != "yes": print("Thanks for playing!")
        break
    
if __name__ == "__main__":
    main()