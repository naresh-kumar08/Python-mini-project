import random
number_to_guess = random.randint(1,100)
while True:
    try:                                                                 # for error handling 
        guess = int(input("Guess the number beetween 1 to 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("too high!")
        else:
            print("Congratulation! You guessed the number")
            break
    except ValueError:
        print("please enter a vailed number")
