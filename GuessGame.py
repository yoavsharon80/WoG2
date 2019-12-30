import random
from Utils import screen_cleaner as clear

def generate_number(difficulty):
    secret = random.randint(1, difficulty)
    # print(secret)
    return secret

def get_guess_from_user(difficulty):
    clear()
    print('Guess A Number Between 1 to', difficulty)
    guess = a = input('Enter Your Number:')
    return guess

def compare_results(difficulty,secret_number):
    guess = input('Enter your Guess:')
    if int(guess) == secret_number:
        return True
    else: return False


def play(difficulty):
    secret = generate_number(difficulty)
    result = compare_results(difficulty,secret)
    if result == True:
        print('You Won!!!!')
        return True
    else:
        print('You Lose')
        return False


# diff = 3
# play(diff)