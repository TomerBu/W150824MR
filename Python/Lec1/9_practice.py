from rock_paper_scissors import  rock, paper, scissors
from random import randint
 
computer_choice = randint(1, 3)

user_choice = int(input("Enter a choice (1: Rock, 2: Paper, 3: Scissors): ")) 

if user_choice == 1:
    # user chose rock
    print(f'user chose {rock}')
    if (computer_choice == 1):
        print(f'Computer chose {rock}')
        print("It's a tie!")
    elif computer_choice == 2:
        print(f'Computer chose {paper}')
        print("You lose!")
    else:
        print(f'Computer chose {scissors}')
        print("You win!")
elif user_choice == 2:
    # user chose paper
    print(f'user chose {paper}')
    if (computer_choice == 1):
        print(f'Computer chose {rock}')
        print("You win!")
    elif computer_choice == 2:
        print(f'Computer chose {paper}')
        print("It's a tie!")
    else:
        print(f'Computer chose {scissors}')
        print("You lose!")
elif user_choice == 3:
    # user chose scissors
    print(f'user chose {scissors}')
    if (computer_choice == 1):
        print(f'Computer chose {rock}')
        print("You lose!")
    elif computer_choice == 2:
        print(f'Computer chose {paper}')
        print("You win!")
    else:
        print(f'Computer chose {scissors}')
        print("It's a tie!")