import os
import time

def screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

def ERROR_MESSAGE():
    e = "Something Went Wrong..."
    return e

def SCORES_FILE_NAME():
    score = 'scores.txt'
    return score

def interval():
    inter = 0.7
    time.sleep(inter)
# print(ERROR_MESSAGE())
# print(SCORES_FILE_NAME())
