import random

def playgame():
    choices = ["rock", "paper", "scissor"]
    user_choice = input("Decide whether rock, paper or scissor: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice")
        return 
    
    computer_choice = random.choice(choices)
    print(f"Computer choosed: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Its a tie!!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You win")
    else:
        print("Computer won!!")

playgame()