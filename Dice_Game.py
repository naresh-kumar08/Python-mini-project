import random
while True:
    choise = (input("Roll the dice(y/n)")).lower()
    if choise == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'{die1},{die2}')
    elif choise == 'n':
        print("Thank you ! for playing")
        break
    else:
        print("Invalid choise! ")

