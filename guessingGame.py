import random
print("Number guessing game")
number = random.randint(1,9)
chances = 0
print("Guess a random number(between 1 and 9):")
while chances < 5 :

    guess = int(input("Enter your guess:-"))

    if guess == number :
        print("Congratulations, you have guessed correctly!")
        break

    elif guess < number :
        print("Sorry, your guess is too low. Guess a number higher than", guess)

    else : 
        print("Sorry, your guess is too high. Guess a number lower than", guess)

    chances += 1

if not chances < 5 :
    print("YOU LOSE!!! The correct number is", number)