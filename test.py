import sys, random
from enum import Enum

name = 'Madden'
age = 30
is_single = True

class RPS(Enum):
    PAPER = 1
    ROCK = 2
    SCISSORS = 3

print(f'Hello World!! My name is {name}!')
print(f'I am {age} years old.')

# print(type(age))

# if isinstance(name, str):
#     print('The name variable is a String')

# if isinstance(age, int):
#     print('The age variable is an int')

## If/Else Statement
# if age >= 30 and name == 'Madden':
        # print('You are Madden!')
# else:
        # print("You are not Madden!")

# Ternary
# print('You are Madden!') if age >= 30 and name == 'Madden' else print('You are not Madden!')

print('What is your name?')
user_name = input('Name: ')
# TODO: Add user input here

if user_name.lower() == 'madden':
    print('Whoa, that\'s my name too!')
else:
    print(f'It is nice to meet you, {user_name.capitalize()}!')

game_choice = input(f'Would you like to play Paper, Rock, Scissors, {user_name.capitalize()}? Please type Yes or No.\n')

def play_game():
 player_choice = input('Choose Paper, Rock, or Scissors. \n Enter 1 for Paper. \n Enter 2 for Rock \n Enter 3 for Scissors \n')

 player = int(player_choice)

 if player < 1 or player > 3:
     print('You must enter 1, 2, or 3.')
 else:
    computer_choice= random.choice("123")

    computer = int(computer_choice)

    print(f'You chose {str(RPS(player)).replace("RPS.", "").capitalize()}')

    print(f'Computer chose chose {str(RPS(computer)).replace("RPS.", "").capitalize()}')
    if player == 1 and computer == 2:
        print("You win!")
    elif player == 2 and computer == 3:
        print("You win!")
    elif player == 3 and computer == 1:
        print("You win!")
    elif player == computer:
        print('It\'s a tie!')
    else:
        print("Computer wins!")

if game_choice.lower() == 'yes':
    play_game()
elif game_choice.lower() == 'no':
    sys.exit('Okay! Goodbye!')
else:
    sys.exit("Please type Yes or No.")

