import Utils
import GuessGame
import MemoryGame
from score import add_score as count


def welcome(player):
    print('Hello', player,'and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play.')

def load_game():
    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    while True:
        game = input('enter game option 1 or 2:')
        if game not in ('1', '2'):
            print(Utils.ERROR_MESSAGE())
            print('enter a valid option')
            continue
        else:
            break
    while True:
        difficulty = input('enter game Difficulty from 1 to 5:')
        if difficulty not in ('1', '2','3','4','5'):
            print(Utils.ERROR_MESSAGE())
            print('enter a valid option')
            continue
        else:
            break
    #casting str from user to int avoid crash
    if int(game) == 1: result = MemoryGame.play(int(difficulty))
    else: result = GuessGame.play(int(difficulty))
    #countint score
    if result == True:
        count(difficulty)
    return(result)

# Utils.screen_cleaner()
# load_game()



