import random

### Program using while loop


while True:
    comp_guess = random.randint(0,10)

    user_guess =  int(input("Kindly enter a number between 0,10: "))

    if user_guess == comp_guess:
        print(f"Congratulations, computer guess = {comp_guess}, your guess is right")
        break
    else:
        print(f"Computer guess = {comp_guess},You loose, try again")

    