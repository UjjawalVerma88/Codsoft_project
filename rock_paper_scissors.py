import random


options = ['rock', 'paper', 'scissors']


player_score = 0
computer_score = 0


while True:
    
    user_choice = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user_choice == 'exit':
        print("\nGame Over!")
        print(f"Final Scores -> You: {player_score}, Computer: {computer_score}")
        break


    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")


    if user_choice not in options:
        print("Invalid choice! Please choose again.")
        continue

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win! Rock crushes scissors.")
            player_score += 1
        else:
            print("You lose! Paper covers rock.")
            computer_score += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win! Paper covers rock.")
            player_score += 1
        else:
            print("You lose! Scissors cut paper.")
            computer_score += 1
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win! Scissors cut paper.")
            player_score += 1
        else:
            print("You lose! Rock crushes scissors.")
            computer_score += 1


    print(f"Score -> You: {player_score}, Computer: {computer_score}")