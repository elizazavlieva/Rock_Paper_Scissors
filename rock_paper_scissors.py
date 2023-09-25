import random

while True:
    result = ''
    user_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print(f'The computer chose {computer_choice}')
        print('Draw!')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('You lose!')
        elif computer_choice == 'scissors':
            print(f'The computer chose {computer_choice}')
            print('You win!')
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print(f'The computer chose {computer_choice}')
            print('You lose!')
        elif computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('You win!')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('You lose!')
        elif computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('You win!')
    else:
        print('Invalid Input. Try again...')
    play_again = input('Play again? (y/n): ')
    if play_again.lower() != 'y':
        break
