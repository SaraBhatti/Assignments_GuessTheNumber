import random

answer = random.randrange(1, 10)

while True:
    try:
        guess = int(input("Enter a number between 1 and 10: "))
        if 1 <= guess <= 10:
            if guess < answer:
                print("Your answer,", guess, "is too low")
            elif guess > answer:
                print("Your answer,", guess, "is too high!")
            else:
                print("Congratulations, you guessed it right!!")
                break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
