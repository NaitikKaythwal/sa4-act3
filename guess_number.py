number = 10
print("I'm thinking of a number...")
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
            print("Sorry, Your number is too high. Try again.")
        else:
            print("Sorry, Your number is too low. Try again.. Try again.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
