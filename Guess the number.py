#Import library
import random

#Random selection of numbers from 1 to 10
answer = random.randrange(1, 10)

#Input a guess
while True:
    try:
        guess = int(input("Enter a number between 1 and 10: "))

#Feedback from your guess
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
            
#Return error if user inputs a value other than 1 to 10
    except ValueError:
        print("Invalid input. Please enter a valid number.")
