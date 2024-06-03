from random  import shuffle


def shuffle_list(input_list):
    shuffle(input_list)
    return input_list

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Input your guess as 0, 1 or 2")
    print("guess", guess)        
    return int(guess)

def check_guess(input_list, guess):
    if input_list[guess] == '0':
        print('Correct guess')
    else:
        print("Wrong guess. Correct position is", input_list)

input_list = [' ', '0', ' ']
check_guess(shuffle_list(input_list), player_guess() )

