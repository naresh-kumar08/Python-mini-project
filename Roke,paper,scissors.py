
import random
user_win = 0
computer_win = 0
while True:
    
    choise = ('r','p','s')
    emoji = {'r':'🪨','p':'📃','s':'✂️'}
    user_choise = input("Choise Roke/paper/scissor(input: r/p/s): ")

    if user_choise == 'q':
        print("Quite Game!")
        break
    elif user_choise not in choise:
        print("Invalid sysntex")
        continue

    computer_choise = random.choice(choise)

    print("You choise: ",emoji[user_choise])
    print("Computer choise: ",emoji[computer_choise])
    
    if computer_choise == user_choise:
        print("TIE!")
    elif (user_choise == 'r' and computer_choise == 's') or \
         (user_choise == 's' and computer_choise == 'p') or \
         (user_choise == 'p' and computer_choise == 'r'):
        print("You win!")
        user_win+=1
        
    else:
        print("computer Win!") 
        computer_win+=1
        
    print("Computer win! ",computer_win,"Time")
    print("You Win! ",user_win,"Time")
    if user_win == 5 or computer_win == 5:
        print("Sorry time limit playing some time letter")
        break