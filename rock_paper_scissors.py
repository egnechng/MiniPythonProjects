import random

user_wins = 0
computer_wins = 0
tie_count = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input!")
        continue

    random_number = random.randint(0, 2)
    # 0-rock, 1-paper, 2-scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == computer_pick:
        print("Tie!")
        continue

    else:
        print("You lose!")
        computer_wins += 1

print("You won", str(user_wins), "times")

print("Computer won", str(computer_wins), "times")
print("Ties:", str(tie_count))


        
