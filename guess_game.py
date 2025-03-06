import random


####Program using if statement


print("Welcome to the game")

comp_guess = input("Kindly enter a number between 0 and 10: ")
rand_guess = random.randint(0,10)

if comp_guess == rand_guess:
    print(f"{comp_guess} is egale to {rand_guess}, therefore you won")
else:
    print(f"{comp_guess} is not egale to {rand_guess}, therefore you loss")