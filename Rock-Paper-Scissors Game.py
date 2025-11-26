import random
user_score = 0
computer_score = 0
while True:
    print("\n Rock Paper Scissors ")
    print("Choose: rock, paper, or scissors")
    user = input("enter your choice: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
