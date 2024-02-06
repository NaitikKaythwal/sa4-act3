number = 10
print("I'm thinking of a number...")
cap=5
while True:
    try:
        guess = input("What number am I thinking of? (Enter 'q' to quit) ")
        if guess == 'q':
            print(f"Sorry! The number was {number}.")
            break
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess > number:
            cap-=1
            if cap==0:
                print(f"Sorry, You ran out of guesses! Better luck next time")
                break
            print(f"Sorry, Your number is too high. You have {cap} guesses left. Try again.")
        else:
            cap-=1
            if cap==0:
                print(f"Sorry, You ran out of guesses! Better luck next time")
                break
            print(f"Sorry, Your number is too low. You have {cap} guesses left. Try again.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
